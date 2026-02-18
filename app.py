from logger import logger 
from src.components.ingestion.load_documents import run_ingestion,run_chunking

def main():
    logger.info("Application started")

    #logger.info("Running ingestion stage")
    #run_ingestion()
    logger.info("Running chunking stage")
    run_chunking()
    #logger.info("Application finished successfully")


if __name__ == "__main__":
    main()
