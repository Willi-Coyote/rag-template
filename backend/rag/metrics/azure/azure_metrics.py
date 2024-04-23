from azure.monitor.opentelemetry.exporter import AzureMonitorMetricExporter
from opentelemetry import metrics
from opentelemetry.sdk.metrics import Histogram
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

from rag.configuration.config import Config


class AzureMetricsManager:
    def __init__(self):
        exporter = AzureMonitorMetricExporter(
            connection_string=Config.azure_monitor_connection_string
        )
        reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)
        metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))

        self._meter = metrics.get_meter_provider().get_meter("rag")
        self._environment = Config().environment or "local"
        self._metrics = {}

    def get_metric(self, metric_name: str):
        full_metric_name = f"{metric_name}_{self._environment}"
        return self._metrics.get(full_metric_name)

    def create_histogram_metric(self, name, description, unit) -> Histogram:
        return self._meter.create_histogram(name=name, description=description, unit=unit)
