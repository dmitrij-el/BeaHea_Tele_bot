import datetime
import logging

from peewee import (CharField, DateTimeField, SqliteDatabase, TextField, DateField,
                    IntegerField, BooleanField, ForeignKeyField)
from peewee import Model, InternalError, PrimaryKeyField




def create_models():
    try:
        Gender.create_table()
        User.create_table()

    except InternalError as pw:
        logging.error()
        print(str(pw))


db_beahea = SqliteDatabase('C:/Users/100Noutbukov/Desktop/python/BeaHeaAdmin/datas/database_beahea.db')



class BaseUserModel(Model):
    class Meta:
        database = db_beahea
        order_by = 'id'


class Gender(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    symbol = CharField()


    class Meta:
        db_table = "gender"



class User(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    creation_time = DateTimeField(default=datetime.datetime.now)
    is_active = BooleanField(default=True)
    user_id = CharField()
    username = CharField()
    name = CharField(max_length=63, null = True)
    surname = CharField(max_length=63, null = True)
    patronymic = CharField(max_length=63, null = True)
    date_birth = DateField(null = True)
    gender = ForeignKeyField(Gender, backref='users', null = True)
    height = IntegerField(null = True)
    weight = IntegerField(null = True)
    phone = CharField(unique=True, index=True, null = True)
    email = CharField(unique=True, index=True, null = True)
    communication_channels = CharField(null = True)


    class Meta:
        db_table = "user"







