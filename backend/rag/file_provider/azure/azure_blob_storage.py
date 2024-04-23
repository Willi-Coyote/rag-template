from typing import List

from azure.storage.blob import BlobServiceClient

from rag.configuration.config import Config
from rag.file_provider.file_provider import FileProvider, FileProxy


class AzureBlobStorage(FileProvider):

    def __init__(self):
        self._account_name: str = Config.account_name
        self._account_key: str = Config.account_key
        self._container_name: str = Config.container_name

        self._connect_str: str = (f"DefaultEndpointsProtocol=https;"
                                  f"AccountName={self._account_name};"
                                  f"AccountKey={self._account_key};"
                                  f"EndpointSuffix=core.windows.net")
        self.blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(
            self._connect_str)

    def get_files_from_directory(self, directory: str) -> List[FileProxy]:
        container_client = self.blob_service_client.get_container_client(self._container_name)
        blob_list = container_client.list_blobs(name_starts_with=directory)

        files = []
        for blob in blob_list:
            url = (f"https://{self._account_name}.blob.core.windows.net/{self._container_name}"
                   f"/{blob.name}")
            file_name = blob.name
            files.append(FileProxy(url=url, file_name=file_name))

        return files
