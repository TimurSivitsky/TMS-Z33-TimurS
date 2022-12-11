from pprint import pprint

from lesson15_HW.settings import intro
from models import *
import uuid
import datetime
from typing import Any


def user_creds_input():
    is_creds_filled: bool = False
    while is_creds_filled is False:
        username = input("username: ")
        if username == 'exit': return False

        password = input("password: ")
        if password == 'exit': return False

        email = input("email: ")
        if email == 'exit': return False

        if Users.is_exist(username=username) == True:
            print(f"User with username: {username} is already exist")
            is_creds_filled = False

        if Users.is_exist(email=email) == True:
            print(f"User with email: {email} is already exist")
            is_creds_filled = False
        else:
            is_creds_filled = True
            return username, password, email


def user_create(username, password, email):
    user = Users.create(user_uuid=uuid.uuid4(), username=username, password=password, email=email,
                        dt_created=datetime.datetime.now())

    print(f"""
        User \'{user.username}\' has been created
        email: {user.email}
        uuid: {user.user_uuid}
                """)

    return user


def registration():
    try:
        data_input = user_creds_input()
        if isinstance(data_input, tuple):
            username = data_input[0]
            password = data_input[1]
            email = data_input[2]
        elif data_input == False:
            return "exit"
    except:
        print("something went wrong in registration module")

    if username and password and email:
        return user_create(username, password, email)


if __name__ == "__main__":
    # print(log_in())
    a = registration()

    print('==========================')
    pprint(a)
