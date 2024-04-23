from typing import List

from langchain.schema import Document

from rag.file_parser.file_parser_factory import FileParser
from rag.file_provider.file_provider import FileProxy


class PdfParser(FileParser):
    def chunk(self, file: FileProxy) -> List[Document]:
        pass
