from unittest.mock import Mock

import pytest

from config.configuration import Configuration
from metrics.aws.aws_open_telemetry import AwsOpenTelemetry
from metrics.azure.azure_open_telemetry import AzureOpenTelemetry
from rag.metrics.open_telemetry_factory import get_open_telemetry, InvalidEnvironmentException


def test_configuration_returns_azure_environment():
    mock_reader = Mock()
    mock_reader.read.side_effect = ["AZURE", "AZURE_CONNECT", "false"]
    config = Configuration(mock_reader)

    assert isinstance(get_open_telemetry(config), AzureOpenTelemetry)


def test_configuration_returns_aws_environment():
    mock_reader = Mock()
    mock_reader.read.side_effect = ["AWS", "AZURE_CONNECT", "false"]
    config = Configuration(mock_reader)

    assert isinstance(get_open_telemetry(config), AwsOpenTelemetry)


def test_configuration_returns_invalid_environment_raises_exception():
    mock_reader = Mock()
    mock_reader.read.side_effect = ["INVALID", "AZURE_CONNECT", "false"]
    config = Configuration(mock_reader)

    with pytest.raises(InvalidEnvironmentException):
        get_open_telemetry(config)
