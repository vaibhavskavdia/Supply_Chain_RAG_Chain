from logger import logger 

class MetadataExtractor:
    #extracts structured metadata for each document
    
    def extract(self,doc_type:str,file_name:str)->dict:
        logger.info(f"Extracting metadata for {file_name}")

        metadata = {
            "doc_type": doc_type,
            "company": "Nestlé",
            "source_file": file_name,
        }

        logger.info(f"Metadata extracted for {file_name}")

        return metadata