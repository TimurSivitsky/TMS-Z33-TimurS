from auth import login
from registration import registration
from tickets import exchange_ticket
from settings import intro


@intro
def welcome_menu():
    choice = input(
        """
        Для взаимодействия используйте команды:
            
        > 1 - Товары
        > 2 - Зарегистрироваться
        > 3 - Войти 
         """)
    match choice:
        case '1':
            # book_list()
            print('Товары()')
            return "Success", 'products'
        case '2':

            reg = registration()
            if reg == 'exit':
                return 'exit'
            if reg is not False:
                return False
        case '3':

            user_and_token = login()
            if user_and_token == 'exit':
                print("Login has been exited by you")
                return 'exit'

            elif isinstance(user_and_token, tuple):
                return user_and_token, 'login'

        case _:
            print(f'неправильный выбор: \'{choice}\'  Попробуйте еще раз\n')
            return False


@intro
def main_menu(user_and_token):
    choice = input(
"""
Для взаимодействия используйте команды:

> 1 - Товары
> 2 - Купить
> 3 - Профиль
> 4 - Тикет 
> 5 - Выйти 
 """)

    match choice:
        case '1':
            # book_list()
            print('Товары()')
            return "Success", 'products'
        case '2':

            reg = registration()
            if reg == 'exit':
                return 'exit'
            if reg is not False:
                return False
        case '4':

            res = exchange_ticket(user_and_token)
            if res == 'exit':
                print("Exchange tickets has been canceled by you")
                return 'exit'

            elif isinstance(user_and_token, tuple):
                return user_and_token, 'login'

        case '3':

            user_and_token = login()
            if user_and_token == 'exit':
                print("Login has been exited by you")
                return 'exit'

            elif isinstance(user_and_token, tuple):
                return user_and_token, 'login'

        case '5':

            user_and_token = login()
            if user_and_token == 'exit':
                print("Login has been exited by you")
                return 'exit'

            elif isinstance(user_and_token, tuple):
                return user_and_token, 'login'

        case _:
            print(f'неправильный выбор: \'{choice}\'  Попробуйте еще раз\n')
            return False

    pass


def session():
    #     print(
    # """
    # =====================================================================
    #                 === Добро пожаловать в "Не магазин" ===
    # =====================================================================
    #
    # Здесь вы можете обменивать тикеты для того, чтобы приобретать товары
    #         """)

    result_item = False
    while result_item is False or result_item == 'exit':
        result_item = welcome_menu()

    if result_item[1] == 'login':
        main_menu(result_item[0])
    if result_item[1] == 'products':
        print("product_view")

    # return result_item


if __name__ == "__main__":
    print(session(), 'adfasdfds')
