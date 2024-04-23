from typing import Protocol

from opentelemetry.sdk.metrics import Histogram

from rag.metrics.azure.azure_metrics import AzureMetricsManager


class MetricsManager(Protocol):
    def get_metric(self, metric_name: str):
        ...

    def create_histogram_metric(self, name, description, unit) -> Histogram:
        ...


metrics_manager = AzureMetricsManager()
