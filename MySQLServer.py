#!/usr/bin/env python3
"""
MySQLServer.py
Creates a database named 'alx_book_store' on a MySQL server.

Requirements:
- If the database already exists, script should not fail.
- Print success message when created successfully.
- Print an error message if connection fails.
- Handle open and close of the DB connection properly.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="your_password_here"  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as err:
        print(f"Error: Could not connect to MySQL server. {err}")

    finally:
       
        if connection.is_connected():
            cursor.close()
            connection.close()
            
if __name__ == "__main__":
    create_database()
