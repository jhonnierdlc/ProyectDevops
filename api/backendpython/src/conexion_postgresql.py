import psycopg2
from fastapi import HTTPException

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host='localhost',
            port='5432',
            user='root',
            password='root',
            database='personas'
        )
        return connection
    except Exception as ex:
        print(f"Error: {ex}")
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")