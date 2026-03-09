from logger import logger


class ContextBuilder:

    """Builds context from retrieved chunks """

    def build_context(self, retrieved_chunks):

        logger.info("Building context from retrieved chunks")

        context_parts = []

        for chunk in retrieved_chunks:

            text = chunk["content"]

            source = chunk["metadata"]["source_file"]

            context_parts.append(
                f"[Source: {source}]\n{text}"
            )

        context = "\n\n".join(context_parts)

        logger.info("Context built successfully")

        return context