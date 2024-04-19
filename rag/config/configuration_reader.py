from typing import Protocol


class ConfigurationReader(Protocol):
    def read(self, key: str) -> str:
        ...


class MissingConfigurationException(Exception):
    def __init__(self, key: str, additional_message: str = ""):
        self.message = (f"No value could be found for the configuration key '{key}'. "
                        f"{additional_message}")
        super().__init__(self.message)
