from ne_magazin.settings import DB_CONNECTION as DB
# from settings import DB_CONNECTION as DB
# from ne_magazin.settings import user_session
# import peewee
import uuid
# print("db connection: ", DB_CONNECTION.connect(), DB_CONNECTION.get_tables())



import datetime
from peewee import *


class Users(DB.Model):
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

    def __str__(self):
        return f"""Profile User INFO
Username:               {self.username}
Email:                  {self.email}
Points:                 {self.points}
Full Name:              {self.fullname}
Phone Number:           {self.phone_number}
Company Name:           {self.company_name}
Registration Date:      {self.dt_created}
Last Login Date:        {self.dt_last_login}
User ID (UUID):         {self.user_uuid}
"""


class UserSession(DB.Model):
    session_uuid = UUIDField(primary_key=True, index=True)
    user_id = ForeignKeyField(Users, field='user_uuid')
    last_login_dt = DateTimeField(default=str(datetime.datetime.now()))
    logout_dt = DateTimeField(null=True, default=None)
    auth_token = CharField(null=False, max_length=255)

    class Meta:
        table_name = "user_session"




class Tickets(DB.Model):
    ticket_uuid = UUIDField(primary_key=True, index=True)
    is_available = BooleanField(default=True)
    user_id = ForeignKeyField(Users, field='user_uuid', null=True, default=None)
    status_change_dt = DateTimeField(default=None, null=True)

    @staticmethod
    def is_ticket_valid(ticket_uuid) -> bool:
        if ticket_uuid:
            try:
                is_ticket_valid = uuid.UUID(ticket_uuid)
                if isinstance(is_ticket_valid, uuid.UUID):
                    ticket: Tickets = Tickets.get(Tickets.ticket_uuid == ticket_uuid)
                    if ticket:
                        if ticket.is_available == True:
                            return True
                        else:
                            return False

            except ValueError as exp:
                # print(exp)
                return False
            except Tickets.DoesNotExist:
                return False
        else: return False

    def __str__(self):
        return f"""Ticket INFO
Ticket ID (UUID):           {self.ticket_uuid}
Available:                  {self.is_available}
Date when was used:         {self.status_change_dt}
"""

class Products(DB.Model):
    product_uuid = UUIDField(primary_key=True, index=True)
    name = CharField(max_length=255, null=False)
    cost = FloatField(default=None, null=False)
    count = IntegerField(default=0, null=False)

    @staticmethod
    def is_exist(product_id):
        try:
            if product_id:
                Products.get(Products.product_uuid == product_id)

        except Products.DoesNotExist:
            raise Products.DoesNotExist("Product not exist")
        else:
            return True


class Orders(DB.Model):
    order_uuid = UUIDField(primary_key=True, index=True)
    user_id = ForeignKeyField(Users, field='user_uuid')
    product_id = ForeignKeyField(Products, field='product_uuid')
    count = IntegerField(default=0)
    order_dt = DateTimeField(default=str(datetime.datetime.now()))


    def __str__(self):
        product_id: Users = self.product_id

        return f"""Order INFO
Order ID (UUID):            {self.order_uuid}
Product:                    {product_id.name}
Count:                      {self.count}
Order Date:                 {self.order_dt}
"""
