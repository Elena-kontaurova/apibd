''' peewee'''
from datetime import datetime
from peewee import MySQLDatabase, Model, IntegerField, CharField, DateTimeField
from pydantic import BaseModel


db = MySQLDatabase('apibd', user='root', password='lenok',
                   host='localhost', port=3306)


class Database(Model):
    ''' d'''
    class Meta:
        ''' j'''
        database = db


class Users(Database):
    ''' Пользователь'''
    id = IntegerField(primary_key=True)
    role_id = IntegerField()
    username = CharField()
    password = CharField()


class Roles(Database):
    ''' roles'''
    id = IntegerField(primary_key=True)
    name = CharField()


class News(Database):
    ''' News'''
    id = IntegerField(primary_key=True)
    heading = CharField()
    content = CharField()
    author = CharField()
    data = DateTimeField(formats=['%Y-%m-%d'])


class Comments(Database):
    ''' Comments'''
    id = IntegerField(primary_key=True)
    news = CharField()
    author = CharField()
    content = CharField()
    data = DateTimeField(formats=['%Y-%m-%d'])


db.connect()
db.create_tables([Users, Roles, News, Comments], safe=True)
db.close()


class UserUpdate(BaseModel):
    ''' kjkj'''
    role_id: int
    username: str
    password: str


class RolesUpdate(BaseModel):
    ''' мг'''
    name: str


class NewsUpdate(BaseModel):
    ''' lk'''
    heading: str
    content: str
    author: str
    data: datetime


class CommentUpdate(BaseModel):
    ''' kj'''
    news: str
    author: str
    content: str
    data: datetime
