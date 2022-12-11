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
    date_created = DateTimeField()
    class Meta:
        table_name = "users"


def forward(old_orm, new_orm):
    users = new_orm['users']
    return [
        # Apply default value datetime.datetime(2022, 12, 11, 2, 56, 39, 840690) to the field users.date_created,
        users.update({users.date_created: datetime.datetime(2022, 12, 11, 2, 56, 39, 840690)}).where(users.date_created.is_null(True)),
    ]
