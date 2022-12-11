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
    points = IntegerField(null=True)
    class Meta:
        table_name = "users"


@snapshot.append
class Tickets(peewee.Model):
    ticket_uuid = UUIDField(index=True, primary_key=True)
    is_available = BooleanField(default=True)
    user_id = snapshot.ForeignKeyField(index=True, model='users', null=True)
    status_change_dt = DateTimeField(null=True)
    class Meta:
        table_name = "tickets"


@snapshot.append
class User_session(peewee.Model):
    session_uuid = UUIDField(index=True, primary_key=True)
    user_id = snapshot.ForeignKeyField(index=True, model='users')
    last_login_dt = DateTimeField(default='2022-12-11 21:54:48.957353')
    logout_dt = DateTimeField(null=True)
    auth_token = CharField(max_length=100)
    class Meta:
        table_name = "user_session"


