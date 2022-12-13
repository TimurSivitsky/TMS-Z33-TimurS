from lesson15_HW.settings import intro
from ne_magazin.models import *
import uuid
import datetime
from typing import Any
from  ne_magazin.views.user_session import create_session


def identification(username) -> bool:
    if Users.is_exist(username=username) == True:
        return Users.is_exist(username=username)
    else:
        print(f"Пользователя {username} не существует")
        return False


def authentication(username, password) -> bool:
    user: Users = Users.get(Users.username == username)
    return str(user.password) == password

def authorization():
    while True:
        # confirmation = input("Yes\\No: ")
        # input_choice = input("> ").replace(' ', '')
        is_unique = False
        print('Введите username и password')
        username = input("username: ").replace(" ", '')
        if bool(username) == False: return False
        password = input("password: ").replace(" ", '')



        if identification(username) == True:
            auth = authentication(username, password)
            if auth == True:
                return create_session(username)
            elif auth == False:
                rtry = input('Wrong password \nWill your try again(Y|N): ')
                match rtry.lower():
                    case 'y':
                        pass
                    case 'n':
                        return False
                    case _:
                        pass
        else:
            rtry = input('Wrong password \nWill your try again(Y|N): ')
            match rtry.lower():
                case 'y':
                    pass
                case 'n':
                    return False
                case _:
                    pass




if __name__ == "__main__":
    print(authorization())
