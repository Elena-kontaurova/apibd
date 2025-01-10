''' peewee'''
from peewee import MySQLDatabase, Model, IntegerField, CharField, DateTimeField


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
    heading = CharField()
    content = CharField()
    author = CharField()
    data = DateTimeField(formats=['%Y-%m-%d'])


class Comments(Database):
    ''' Comments'''
    news = CharField()
    author = CharField()
    content = CharField()
    data = DateTimeField(formats=['%Y-%m-%d'])


db.connect()
db.create_tables([Users, Roles, News, Comments], safe=True)
db.close()
