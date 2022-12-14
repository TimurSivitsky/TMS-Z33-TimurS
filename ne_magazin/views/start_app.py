from ne_magazin.settings import menu_items_map, intro
from ne_magazin.views.registration import registration
from ne_magazin.views.login import authorization
from ne_magazin.views.second_app_view import launch_second_view
from ne_magazin.views.products import products_list_view, create_default_product
from ne_magazin.views.tickets import create_default_tickets


import time


@intro
def render_start_menu():
    while True:
        # print(welcome_msg)
        print(
            f"""
Для взаимодействия выберете номер команды:

> 1 - {menu_items_map['login_view'][0]}
> 2 - {menu_items_map['login_view'][1]}
> 3 - {menu_items_map['login_view'][2]}
> 4 - {menu_items_map['login_view'][3]}
        """)
        input_choice = input("> ").replace(' ', '')

        match input_choice:
            case '1':
                return "Товары"
            case '2':
                return "Регистрация"
            case '3':
                return "Авторизация"

            case '4':
                print("Apps will closed in 3 sec")
                time.sleep(3)
                exit()
                return 'exit'

            case _:
                print(f'неправильный выбор: \'{input_choice}\'  Попробуйте еще раз')


def executer():
    exit_obj = render_start_menu()
    match exit_obj:
        case "Регистрация":
            print('reg')
            # registration()

            exit_obj = registration()
            if exit_obj == False:
                return False
            if bool(exit_obj) == True:
                return False
        case "Авторизация":
            try:
                print('auth')
                exit_obj = authorization()
                if exit_obj == False:
                    return False
                if bool(exit_obj) == True:
                    return "authorized", exit_obj
            except Exception as e:
                return False

            # exit_obj = authorization_module(exit_obj)
        case "Товары":
            print('products')
            exit_reslut = products_list_view()
            return exit_reslut
            # exit_obj = product_module(exit_obj)



def launch():
    create_default_product(5)
    create_default_tickets(5)
    print('Created randomly default tickets, and products')

    while True:
        a = executer()
        while a == False:
            a = executer()
            if a == "exit":
                return 'exit'

        while bool(a) == True:
            if isinstance(a, tuple):
                if a[0] == 'authorized':
                    res = launch_second_view(a[1])
                    if res == "Logout":
                        break


if __name__ == "__main__":
    launch()
