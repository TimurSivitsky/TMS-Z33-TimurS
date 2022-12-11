# from lesson15_HW.settings import DB_CONNECTION
import datetime
import datetime
from peewee import *
import peewee

DB_USER_ENV: dict = {
    "db_name": "lesson15",
    "username": "postgres",
    "password": "123!@#qweQWE",
    "environment": "localhost",
    'port': 5432,
}

DB_CONNECTION = peewee.PostgresqlDatabase(database=DB_USER_ENV['db_name'], host=DB_USER_ENV["environment"],
                                          port=DB_USER_ENV['port'], user=DB_USER_ENV['username'],
                                          password=DB_USER_ENV['password'])

print("db connection: ", DB_CONNECTION.connect(), DB_CONNECTION.get_tables())


class Users(DB_CONNECTION.Model):
    user_uuid = UUIDField(primary_key=True, index=True)
    fullname = CharField(max_length=40, null=True)
    username = CharField(max_length=40, unique=True, null=False)
    password = CharField(max_length=128, null=False, )
    email = CharField(max_length=100, unique=True)
    phone_number = CharField(max_length=12, null=True)
    company_name = CharField(max_length=100, null=True)
    dt_created = DateTimeField()
    dt_last_login = DateTimeField(default=None, null=True)
    points = IntegerField(default=0)

    @staticmethod
    def is_exist(username=None, email=None) -> bool:
        try:
            if username:
                Users.get(Users.username == username)
            if email:
                Users.get(Users.email == email)

        except Users.DoesNotExist:
            return False
        else:
            return True


class User_session(DB_CONNECTION.Model):
    session_uuid = UUIDField(primary_key=True, index=True)
    user_id = ForeignKeyField(Users, field='user_uuid')
    last_login_dt = DateTimeField(default=str(datetime.datetime.now()))
    logout_dt = DateTimeField(null=True, default=None)
    auth_token = CharField(null=False, max_length=100)


class Tickets(DB_CONNECTION.Model):
    ticket_uuid = UUIDField(primary_key=True, index=True)
    is_available = BooleanField(default=True)
    user_id = ForeignKeyField(Users, field='user_uuid', null=True)
    status_change_dt = DateTimeField(default=None, null=True)

    @staticmethod
    def is_ticket_valid(ticket_uuid) -> bool:
        try:
            if ticket_uuid:
                ticket: Tickets = Tickets.get(Tickets.ticket_uuid == ticket_uuid)
                if ticket:
                    if ticket.is_available == True:
                        return True
                    else:
                        return False
        except Tickets.DoesNotExist:
            return False
        else:
            return True
