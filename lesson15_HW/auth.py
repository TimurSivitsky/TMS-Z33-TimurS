from lesson15_HW.settings import intro
from models import *
import uuid
import datetime
from typing import Any


def user_creds_input() -> dict:
    # is_creds_filled: bool = False
    username, password = "", ""

    while bool(username) == False:
        username = input("username: ").replace(" ", '')
        if username == "exit": return 'exit'
    while bool(password) == False:
        password = input("password: ").replace(" ", '')
        if password == "exit": return 'exit'

    return username, password


def auth(creds: tuple):
    # if isinstance(creds, tuple):
    username = creds[0]
    password = creds[1]
    # else: return False

    if Users.is_exist(username):
        try:
            user = Users.get(Users.username == username)
            if str(user.password) == password:
                token: str = f'token_{username}_{datetime.datetime.now()}'
                return user, token
                # return f'access token: {"abcd_token"}, user {user.username},{user.email}, UUID - {user.user_uuid}', user
            else:
                # return f"No active user with that credentials, WRONG PASSWORD, Lets try again"
                return False
        except Exception as exs:
            print(f'Something went wrong {user} - {user.username}, {password} - {user.password} \n {exs}')
    else:
        return False


def create_session(user, token):
    User_session.create(session_uuid=uuid.uuid4(), user_id=user.user_uuid,
                        auth_token=token)
    user_upd = Users.get(Users.user_uuid == user.user_uuid)
    user_upd.dt_last_login = datetime.datetime.now()
    user_upd.save()


def login():
    # try:
    is_ok: bool = False
    while is_ok == False:
        print("\nEnter Login Creds ")
        creds = user_creds_input()
        if creds == 'exit':
            return 'exit'

        data = auth(creds)
        if isinstance(data, tuple):
            is_ok = True
            create_session(data[0], data[1])
            return data
        elif data == False:
            is_ok = False

    # except:
    #     return "something went wrong in registration module"


# def login():
#     # try:
#     #     while auth(user_creds_input()) == False:
#     #         auth(user_creds_input())
#     #
#     #     data_input = user_creds_input()
#     #     if isinstance(data_input, tuple):
#     #         username = data_input[0]
#     #         password = data_input[1]
#     #
#     #
#     #
#     #         try:
#     #             if username and password:
#     #                 res = auth(username, password)
#     #                 if isinstance(res, tuple):
#     #                     return res
#     #                 if isinstance(res, bool):
#     #
#     #
#     #     elif data_input == False:
#     #         return "exit"
#     # except:
#     #     "something went wrong in auth module"
#     #
#     # if username and password:
#     #     res = auth(username, password)
#     #     if isinstance(res, tuple):
#     #         return res
#     #     if isinstance(res, bool):
#     #
#     #
#     #
#     #
#
#     try:
#         data = auth(user_creds_input())
#         # is_auth = False
#         while data == False:
#             print('\nEnter your creds for auth')
#             if isinstance(data, tuple):
#                 # is_auth = True
#                 data, token = auth(user_creds_input())
#             elif data == False:
#                 data = False
#
#         if bool(data) is True and bool(data) is True:
#             User_session.create(session_uuid=uuid.uuid4(), user_id=data.user_uuid,
#                                 auth_token=token)
#         return auth_token
#     except BaseException as e:
#         print(e)
#         return False


if __name__ == "__main__":
    print(login())
