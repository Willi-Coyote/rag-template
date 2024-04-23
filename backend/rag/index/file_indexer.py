from typing import List

from langchain.schema import Document

from rag.file_parser.file_parser_factory import FileParser, create_file_parser
from rag.file_provider.file_provider import FileProvider, FileProxy
from rag.logs.logger import logger
from rag.tools.timer import MetricBenchmarkTimer
from rag.vector_store.vector_store import VectorStore


class FileIndexer:
    def __init__(self, file_provider: FileProvider, vector_store: VectorStore):
        self._file_provider = file_provider
        self._vector_store = vector_store

    def index_files(self, directory: str):
        files = self._file_provider.get_files_from_directory(directory)
        logger.info(f"Found {len(files)} files in directory '{directory}' to index.")
        for file in files:
            self.index_file(file)

    def index_file(self, file: FileProxy):
        with MetricBenchmarkTimer("Index file timer", log=True):
            logger.info(f"Start indexing file '{file.file_name}'")
            chunks = self._parse_file(file)
            self._vector_store.add_documents(chunks)


    def _parse_file(self, file: FileProxy) -> List[Document]:
        file_parser: FileParser = create_file_parser(file.file_name)
        chunks = file_parser.chunk(file=file)
        logger.info(f"Parsed and split file '{file.file_name}' into {len(chunks)} chunks")
        return chunks
