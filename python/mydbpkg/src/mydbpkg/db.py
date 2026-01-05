import os
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return connect(
        host=os.getenv("DATABASE_host"),
        user=os.getenv("DATABASE_user"),
        password=os.getenv("DATABASE_passwd"),
        database=os.getenv("DATABASE_database"),
    )
