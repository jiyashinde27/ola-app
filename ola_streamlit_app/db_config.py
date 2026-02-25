import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="qwertyuiopmnbvcxz!@12",
        database="ola"
    )