import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
host,username,password = os.getenv('HOST_NAME'), os.getenv('USER'), os.getenv('PASSWORD')



def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection(host, username, password)