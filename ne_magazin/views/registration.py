from pprint import pprint

from lesson15_HW.settings import intro
from ne_magazin.models import *
import uuid
import datetime
from typing import Any


def is_unique_new_user(username, email) -> bool:
    # is_unique = None
    # is_unique_username = None
    # is_unique_email = None
    if Users.is_exist(username=username) == True:
        print(f'Юзер с таким username: "{username}" уже существует в системе ')
        is_unique_username = False
    else:
        is_unique_username = True
    if Users.is_exist(email=email) == True:
        print(f'Юзер с таким email: "{email}" уже существует в системе\n')
        is_unique_email = False
    else:
        is_unique_email = True
    return is_unique_email and is_unique_username


def user_create(username, password, email) -> bool:
    try:
        user = Users.create(user_uuid=uuid.uuid4(), username=username, password=password, email=email,
                            dt_created=datetime.datetime.now())
        print(
            f"""
======================================================
||    User:\t\t {user.username} был создан
||    email:\t {user.email}
||    uuid:\t\t {user.user_uuid}
======================================================
""")
        return user
    except Exception as e:
        print("ERROR DB CREATION USER", e)
        return False


def registration():
    while True:
        # confirmation = input("Yes\\No: ")
        # input_choice = input("> ").replace(' ', '')
        is_unique = False
        username = input("username: ")
        password = input("password: ")
        email = input("email: ")
        result_of_uniqueness = is_unique_new_user(username, email)
        if result_of_uniqueness == True:
            return user_create(username, password, email)
        elif result_of_uniqueness == False:
            rtry = input('Will your try again(Y|N): ')
            match rtry.lower():
                case 'y': pass
                case 'n': return False
                case _: pass


if __name__ == "__main__":
    # print(log_in())
    a = registration()

    # print('==========================')
    pprint(a)
