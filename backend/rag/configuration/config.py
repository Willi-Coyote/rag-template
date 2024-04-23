from confz import BaseConfig, EnvSource


class Config(BaseConfig):
    azure_blob_storage_account_name: str
    azure_blob_storage_account_key: str
    azure_blob_storage_container_name: str

    environment: str = "local"

    CONFIG_SOURCES = EnvSource()
