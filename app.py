from logger import logger 
from src.components.ingestion.load_documents import run_ingestion,run_chunking
from src.components.embeddings.run_embedding import run_embedding
def main():
    logger.info("Application started")
    #ingestion stage
    logger.info("Running ingestion stage")
    run_ingestion()
    #chunking stage
    logger.info("Running chunking stage")
    run_chunking()
    #embedding stage
    logger.info("Running embedding stage")
    run_embedding()
    logger.info("Application finished successfully")


if __name__ == "__main__":
    main()
