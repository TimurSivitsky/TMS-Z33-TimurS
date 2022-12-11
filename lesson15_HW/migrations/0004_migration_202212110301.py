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


def backward(old_orm, new_orm):
    users = new_orm['users']
    return [
        # Apply default value datetime.datetime(2022, 12, 11, 3, 1, 0, 248240) to the field users.dt_last_login,
        users.update({users.dt_last_login: datetime.datetime(2022, 12, 11, 3, 1, 0, 248240)}).where(users.dt_last_login.is_null(True)),
    ]
