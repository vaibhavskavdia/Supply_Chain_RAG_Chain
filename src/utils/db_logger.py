import psycopg2
import json
from datetime import datetime


class RAGDatabaseLogger:

    def __init__(self):

        self.conn = psycopg2.connect(
            host="localhost",
            database="rag_copilot",
            user="postgres",
            password="postgresql",
            port="5433"
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