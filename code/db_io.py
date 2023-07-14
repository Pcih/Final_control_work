"""
Взаимодейсвие с базой данных MySQL
"""
import os
import mysql.connector
from mysql.connector import connection
import dotenv

dotenv.load_dotenv()

USER = os.getenv('DB_USER')
PASSW = os.getenv('DB_PASSW')
DB_NAME = os.getenv('DB_NAME')


def connect_to_database(func):
    def wrapper(*args, **kwargs):
        connection = mysql.connector.connect(
            host='localhost',
            user=USER,
            password=PASSW,
            database=DB_NAME
        )
        cursor = connection.cursor()
        result = func(cursor, connection, *args, **kwargs)
        cursor.close()
        connection.close()
        return result

    return wrapper


@connect_to_database
def load_all_data(cursor: connection.MySQLCursor, connection: connection.MySQLConnection):
    cursor.execute("SELECT id, name, date_of_birth, commands, specie FROM all_animals")
    return cursor.fetchall()


@connect_to_database
def add_new_animal(cursor: connection.MySQLCursor, connection: connection.MySQLConnection,
                   name, date_of_birth, specie):
    cursor.execute("INSERT INTO all_animals (name, date_of_birth, specie, commands) VALUES "
                   "(%s, %s, %s, '')", (name, date_of_birth, specie))
    connection.commit()
    cursor.execute("SELECT id FROM all_animals WHERE id = LAST_INSERT_ID()")
    db_id = cursor.fetchall()[0][0]
    return db_id


@connect_to_database
def update_command(cursor: connection.MySQLCursor, connection: connection.MySQLConnection, db_id, commands):
    commands = ','.join(commands)
    cursor.execute("UPDATE all_animals SET commands = %s WHERE id = %s", (commands, db_id))
    connection.commit()


@connect_to_database
def delete_animal(cursor: connection.MySQLCursor, connection: connection.MySQLConnection, db_id):
    cursor.execute("DELETE FROM all_animals WHERE id = %s", (db_id,))
    connection.commit()
