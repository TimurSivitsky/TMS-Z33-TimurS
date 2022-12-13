import uuid
import datetime

import jwt
from ne_magazin.models import *

dt = datetime.datetime.now()

def generate_token(user: Users):
    token_data = {
        "uuid": str(user.user_uuid),
        "username": str(user.username),
        "email": str(user.email),
        "last_login": str(dt)
    }
    jwt_token: jwt = jwt.encode(token_data, "tima_secret", algorithm="HS256")
    print(jwt_token)
    return str(jwt_token)


def create_session(username):
    try:
        user: Users = Users.get(Users.username == username)
        token = generate_token(user)

        UserSession.create(session_uuid=uuid.uuid4(), user_id=user.user_uuid,
                           auth_token=token, last_login_dt=dt)
        user.dt_last_login = dt
        user.save()
        return token
    except Exception as exc:
        print(f"creation session has been blocked: {exc}")
        return False
