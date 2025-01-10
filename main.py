''' main для fastapi + mysql'''
from datetime import datetime
from fastapi import FastAPI
from connect import Users, Roles, News, Comments, db


app = FastAPI()


# Запросы на просмотр


def get_all_users_db():
    ''' получение всех users'''
    users = Users.select()
    return [{'id': user.id, 'role_id': user.role_id, 'username': user.username}
            for user in users]


def get_all_roles_db():
    ''' Получение всех roles'''
    role = Roles.select()
    return [{'id': ro.id, 'name': ro.name} for ro in role]


def get_all_news_db():
    ''' Получение всех news'''
    new = News.select()
    return [{'id': ne.id, 'heading': ne.heading, 'content': ne.content,
            'author': ne.author, 'data': ne.data}
            for ne in new]


def get_all_comment_db():
    ''' Получение всех comments'''
    com = Comments.select()
    return [{'id': comm.id, 'news': comm.news, 'author': comm.author,
             'content': comm.content, 'data': comm.data}
            for comm in com]


# Запросы на создание


def create_user_db(role_id: int, username: str, password: str):
    ''' Создание нового пользователя Users'''
    user = Users.create(role_id=role_id, username=username, password=password)
    return {
        'id': user.id,
        'role_id': user.role_id,
        'username': user.username,
        'password': user.password,
    }


def create_roles_db(name: str):
    ''' Создание записи Roles'''
    role = Roles.create(name=name)
    return {
        'id': role.id,
        'name': role.name
    }


def create_news_db(heading: str, content: str, author: str, data: datetime):
    ''' Создание записи News'''
    new = News.create(heading=heading, content=content,
                      author=author, data=data)
    return {
        'heading': new.heading,
        'content': new.content,
        'author': new.author,
        'data': new.data
    }


def create_comment_db(news: str, author: str, content: str, data: datetime):
    ''' Создание записи comment'''
    com = Comments.create(news=news, author=author, content=content, data=data)
    return {
        'news': com.news,
        'author': com.author,
        'content': com.content,
        'data': com.data
    }


# Методы просмотра


@app.get('/users')
def get_all_users():
    ''' Получение всех users'''
    return get_all_users_db()


@app.get('/roles')
def get_all_roles():
    ''' Получение всез roles'''
    return get_all_roles_db()


@app.get('/news')
def get_all_news():
    ''' получение всех news'''
    return get_all_news_db()


@app.get('/comment')
def get_all_comment():
    ''' Получение всез comment'''
    return get_all_comment_db()


# Методы создания


@app.post('/user_create')
def create_user(role_id: int, username: str, password: str):
    ''' Создание новой записи users'''
    return create_user_db(role_id, username, password)


@app.post('/roles_create')
def create_roles(name: str):
    ''' Создание новой записи roles'''
    return create_roles_db(name)


@app.post('/news_create')
def create_news(heading: str, content: str, author: str, data: datetime):
    ''' Создание новой записи news'''
    return create_news_db(heading, content, author, data)


@app.post('/comment_create')
def create_comment(news: str, author: str, content: str, data: datetime):
    ''' Создание новой записи comment'''
    return create_comment_db(news, author, content, data)


db.connect()
db.close()
