from typing import Protocol


class OpenTelemetry(Protocol):
    def configure(self):
        ...
