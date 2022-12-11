import peewee
import psycopg2

# DB_USER_ENV: dict = {
#     "db_name": "lessondb",
#     "username": "postgres",
#     "password": "123!@#qweQWE",
#     "environment": "localhost",
#     'port': 5432,
# }
#
# DB_CONNECTION = peewee.PostgresqlDatabase(database=DB_USER_ENV['db_name'], host=DB_USER_ENV["environment"],
#                                           port=DB_USER_ENV['port'], user=DB_USER_ENV['username'],
#                                           password=DB_USER_ENV['password'])
#
#
# print("db connection: ", DB_CONNECTION.connect())


tamplate_msg = {
    'status_code': int,
    'result': [dict],

}


def intro(func):
    def new_func(*args, **kwargs):
        print(
"""
=====================================================================
                === Добро пожаловать в "Не магазин" ===
=====================================================================

Здесь вы можете обменивать тикеты для того, чтобы приобретать товары
        """)
        result = func(*args,**kwargs)
        return result
    return new_func
