from datetime import datetime

from opentelemetry.sdk.metrics import Histogram

from rag.logs.logger import logger
from rag.metrics.metrics import metrics_manager


class BenchmarkTimer:
    def __init__(self, name=""):
        """
        Initialize the benchmark timer with an optional name.

        :param name: A string that identifies the block of code being timed.
                     If provided, it will be included in the final output message which looks like
                     "The execution of '<name>' took 15.87s to run"
        """
        self._name = name

    def __enter__(self):
        self.start_time = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        execution_time = datetime.now() - self.start_time
        logger.info(f"The execution of '{self._name}' took {execution_time.total_seconds():.2f}s "
                    f"to run")


class MetricBenchmarkTimer:
    def __init__(self, metric_name: str, log: bool = False):
        """
        Initialize the benchmark timer with a metric name and a flag that indicates whether the
        execution time should be logged in addition (default is False).

        :param metric_name: The name of the metric that is being measured. The execution time will
                            be published under this metric name
        :param log: A boolean flag that indicates whether the execution time should be logged in
                    addition
        """
        self._metric_name = metric_name
        self._log = log

    def __enter__(self):
        self.start_time = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        execution_time = datetime.now() - self.start_time

        self._update_metric(execution_time)

        if self._log:
            logger.info(f"The task took {execution_time.total_seconds():.2f}s to run")

    def _update_metric(self, execution_time):
        metric = metrics_manager.get_metric(self._metric_name)
        if metric is None:
            metric = self._create_metric()
        metric.record(execution_time.total_seconds())

    def _create_metric(self) -> Histogram:
        description = "Execution time of '{self._metric_name}'"
        return metrics_manager.create_histogram_metric(name=self._metric_name,
                                                       description=description, unit="s")
