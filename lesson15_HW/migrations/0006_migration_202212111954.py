# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Users(peewee.Model):
    user_uuid = UUIDField(index=True, primary_key=True)
    fullname = CharField(max_length=40, null=True)
    username = CharField(max_length=40, unique=True)
    password = CharField(max_length=128)
    email = CharField(max_length=100, unique=True)
    phone_number = CharField(max_length=12, null=True)
    company_name = CharField(max_length=100, null=True)
    dt_created = DateTimeField()
    dt_last_login = DateTimeField(null=True)
    class Meta:
        table_name = "users"


@snapshot.append
class User_session(peewee.Model):
    session_uuid = UUIDField(index=True, primary_key=True)
    user_id = snapshot.ForeignKeyField(index=True, model='users')
    last_login_dt = DateTimeField(default='2022-12-11 19:54:13.932515')
    logout_dt = DateTimeField(null=True)
    auth_token = CharField(max_length=100)
    class Meta:
        table_name = "user_session"


def forward(old_orm, new_orm):
    user_session = new_orm['user_session']
    return [
        # Apply default value '' to the field user_session.auth_token,
        user_session.update({user_session.auth_token: ''}).where(user_session.auth_token.is_null(True)),
    ]
