import mysql.connector
from mysql.connector import MySQLConnection

def get_connection() -> MySQLConnection:
    return mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="library",
        autocommit=True
    )
    