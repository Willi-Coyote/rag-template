from config.configuration_reader import ConfigurationReader
from config.dotenv_configuration import DotEnvConfigurationReader


class Configuration:
    def __init__(self, reader: ConfigurationReader = DotEnvConfigurationReader()):
        self._reader = reader

        self._environment = self._reader.read("ENVIRONMENT")
        self._azure_app_insights_connection_string = self._reader.read(
            "AZURE_APP_INSIGHTS_CONNECTION_STRING")
        self._token_validation = self._reader.read("TOKEN_VALIDATION")
        # self._audience = self._reader.read("AUDIENCE")
        # self._issuer_url = self._reader.read("ISSUER_URL")

    @property
    def azure_app_insights_connection_string(self):
        return self._azure_app_insights_connection_string

    @property
    def environment(self):
        return self._environment

    @property
    def token_validation(self):
        return self._token_validation

    @property
    def audience(self):
        return self.audience

    @property
    def issuer_url(self):
        return self.issuer_url
