from typing import List, Protocol


class FileProxy:
    def __init__(self, url: str, file_name: str):
        self.url = url
        self.file_name = file_name


class FileProvider(Protocol):

    def get_files_from_directory(self, directory: str) -> List[FileProxy]:
        ...
