from typing import Protocol, List, Any

from langchain.schema import Document


class VectorStore(Protocol):
    def add_documents(self, documents: List[Document], **kwargs: Any) -> List[str]:
        ...
