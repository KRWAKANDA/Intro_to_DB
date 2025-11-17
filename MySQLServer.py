# MySQLServer.py

import mysql.connector
from mysql.connector import Error
# MySQLServer.py

import mysql.connector

def create_database():
    connection = None
    cursor = None

    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = connection.cursor()

        # Create the database without using SELECT or SHOW
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

def create_database():
    try:
        # Connect to MySQL Server (update host, user, password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close connection safely
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.")  # Optional

if __name__ == "__main__":
    create_database()

