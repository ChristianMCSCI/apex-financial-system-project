import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_database_connection():
    """Establishes and returns a connection to the MySQL database."""
    try:
        connection = pymysql.connect(
            host= os.getenv("DB_HOST"),
            user= os.getenv("DB_USER"),       
            password= os.getenv("DB_PASSWORD"), 
            database= os.getenv("DB_NAME")
        )
        print("Database connection successfully established.")
        return connection
        
    except pymysql.MySQLError as e:
        print(f"CRITICAL: Failed to connect to the database. Error: {e}")
        return None