class Document:
    """
    Core document model used across ingestion, chunking,
    embeddings and retrieval.
    """

    def __init__(self, content: str, metadata: dict):
        self.content = content
        self.metadata = metadata
