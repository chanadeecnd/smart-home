import mysql.connector
from contextlib import contextmanager


class Database:

    def __init__(self, database):
        self.__config = {
            'user': 'root',
            'password': 'admin1234',
            'host': '127.0.0.1',
            'database': database
        }

    @contextmanager
    def __connect(self):
        connection = mysql.connector.connect(**self.__config)
        cursor = connection.cursor(dictionary=True)
        try:
            yield connection, cursor
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")

    def insert_data(self, table_name, data):
        try:
            with self.__connect() as (connection, cursor):
                cursor.execute(f"SELECT MAX(id) FROM {table_name}")
                last_id = cursor.fetchone()
                new_data = self.__generate_data_tuple(data, last_id)

                query = f"INSERT INTO {table_name} VALUES (%s, %s, %s)"
                cursor.execute(query, new_data)
                connection.commit()
                print(f"Data inserted, ID: {cursor.lastrowid}")

        except mysql.connector.Error as e:
            print(f"Error while connecting to MySQL", e)

    def __generate_data_tuple(self, data: dict, last_id):
        print(last_id, data)
        new_id = int(last_id['MAX(id)']) + 1
        data_tuple = tuple(data.values())
        return (new_id,) + data_tuple

# การใช้งาน
# mydb = Database("coniglink")
# data = {'username':'test4', 'password':'world'}
# mydb.insert_data(table_name='users', data=data)
