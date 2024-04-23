from typing import List

from langchain.schema import Document

from rag.file_parser.docx_parser import DocxParser
from rag.file_parser.pdf_parser import PdfParser
from rag.file_provider.file_provider import FileProxy


class FileParser:
    def chunk(self, file: FileProxy) -> List[Document]:
        pass


def create_file_parser(file_name: str) -> FileParser:
    if file_name.endswith('.pdf'):
        return PdfParser()
    elif file_name.endswith('.docx'):
        return DocxParser()
    else:
        raise ValueError(f"Cannot find a parser for the file '{file_name}'")
