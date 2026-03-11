import psycopg2
import json
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

class RAGDatabaseLogger:

    def __init__(self):

        self.conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=os.getenv("POSTGRES_PORT")
        )

        self.cursor = self.conn.cursor()

    def log_query(self, query, retrieved_chunks, sources, answer, latency):

        insert_query = """
        INSERT INTO rag_query_logs
        (timestamp, query, retrieved_chunks, sources_used, answer, latency)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        self.cursor.execute(
            insert_query,
            (
                datetime.utcnow(),
                query,
                json.dumps(retrieved_chunks),
                json.dumps(sources),
                answer,
                latency
            )
        )

        self.conn.commit()