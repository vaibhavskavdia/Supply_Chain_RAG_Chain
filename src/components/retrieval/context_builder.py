from logger import logger


class ContextBuilder:

    """Builds context from retrieved chunks"""

    def build_context(self, retrieved_chunks, max_chunks=5):

        logger.info("Building context for LLM")

        context_parts = []
        sources = []

        # Sort chunks by similarity (highest first)
        retrieved_chunks = sorted(
            retrieved_chunks,
            key=lambda x: x.get("similarity", 0),
            reverse=True
        )

        for i, chunk in enumerate(retrieved_chunks[:max_chunks], start=1):

            metadata = chunk.get("metadata", {})

            source_file = metadata.get("source_file", "Unknown")
            chunk_index = metadata.get("chunk_index", "N/A")

            similarity = chunk.get("similarity", 0)

            source_info = {
                "id": i,
                "document": source_file,
                "chunk": chunk_index,
                "similarity": similarity
            }

            sources.append(source_info)

            chunk_text = chunk.get("content", "")

            context_parts.append(
                f"[Source {i} | {source_file} | Chunk {chunk_index} | Score {similarity:.2f}]\n{chunk_text}"
            )

        context = "\n\n".join(context_parts)

        logger.info(f"Context built using {len(sources)} chunks")

        return context, sources