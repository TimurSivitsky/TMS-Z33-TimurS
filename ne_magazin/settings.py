import peewee

# from models import Users

DB_USER_ENV: dict = {
    "db_name": "lesson15",
    "username": "postgres",
    "password": "123!@#qweQWE",
    "environment": "localhost",
    'port': 5432,
}
menu_items_map: dict = {
    'login_view': ['Товары', "Зарегистрироваться", "Войти", "Закрыть приложение"],
    "after_login_view": ["Товары", "Купить", "Профиль", "Тикет", "Логаут"]
}

welcome_msg = """
=====================================================================
                === Добро пожаловать в "Не магазин" ===
=====================================================================

Здесь вы можете обменивать тикеты для того, чтобы приобретать товары
"""

DB_CONNECTION = peewee.PostgresqlDatabase(database=DB_USER_ENV['db_name'], host=DB_USER_ENV["environment"], port=DB_USER_ENV['port'], user=DB_USER_ENV['username'], password=DB_USER_ENV['password'])

user_session = ''

print("db connection: ", DB_CONNECTION.connect(), DB_CONNECTION.get_tables())


def intro(func):
    def new_func(*args, **kwargs):
        print(welcome_msg)

        result = func(*args, **kwargs)
        return result

    return new_func
