from config.configuration import Configuration
from metrics.aws.aws_open_telemetry import AwsOpenTelemetry
from metrics.azure.azure_open_telemetry import AzureOpenTelemetry
from metrics.open_telemetry import OpenTelemetry


def get_open_telemetry(config: Configuration) -> OpenTelemetry:
    environment = config.environment
    if environment == "AZURE":
        return AzureOpenTelemetry(config)
    elif environment == "AWS":
        return AwsOpenTelemetry(config)
    else:
        raise InvalidEnvironmentException(environment)


class InvalidEnvironmentException(Exception):
    def __init__(self, environment: str):
        self.environment = environment
        super().__init__(f"The environment: '{environment}' is not supported. Valid values are "
                         f"'AZURE' and 'AWS'.")
