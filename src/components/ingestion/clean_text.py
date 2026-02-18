import re 
from logger import logger


#cleans raw pdf text to remove unwanted characters and formatting before chunking and embedding

class TextCleaner:
    def clean_text(self,text:str)->str:
       logger.info("Starting cleaning text")
       
       #remove excessive new lines
       text=re.sub(r"\n+","\n",text)
       
       #remove page numbers
       text=re.sub(r"Page\s+\d+\n","",text)
       
       #remove standalone numbers
       text = re.sub(r"\n\d+\n", "\n", text)
       
       #remove whitespaces
       text = re.sub(r"\s+", " ", text)
       logger.info("Finished cleaning text")
       
       cleaned_text=text.strip()
       return cleaned_text
   