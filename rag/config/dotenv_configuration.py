import os

from config.configuration_reader import ConfigurationReader, MissingConfigurationException


class DotEnvConfigurationReader(ConfigurationReader):
    def read(self, key: str) -> str:
        try:
            return os.environ[key]
        except KeyError:
            additional_message = "Please check your .env file and ensure that the key is set"
            raise MissingConfigurationException(key, additional_message)
