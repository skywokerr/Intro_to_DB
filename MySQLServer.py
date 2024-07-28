import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',        # MySQL server host
            user='root',             # MySQL username
            password='maryannwacuka4' # MySQL password
        )
        
        if connection.is_connected():
            print("Connected to MySQL server")

            # Create a cursor object
            cursor = connection.cursor()

            # SQL statement to create a database if it does not exist
            create_db_query = """
            CREATE DATABASE IF NOT EXISTS alx_book_store;
            """
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()