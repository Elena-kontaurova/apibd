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


# Запросы на редактирования

def update_users_db(user_id: int, role_id: int, username: str, password: str):
    ''' Обновление записи пользователя '''
    user = Users.get(Users.id == user_id)
    user.role_id = role_id
    user.username = username
    user.password = password
    user.save()
    return {
        'id': user.id,
        'role_id': user.role_id,
        'username': user.username,
        'password': user.password
    }


def update_roles_db(rol_id: int, name: str):
    ''' Обновление roles'''
    rol = Roles.get(Roles.id == rol_id)
    rol.name = name
    rol.save()
    return {
        'id': rol.id,
        'name': rol.name
    }


def update_news_db(new_id: int, heading: str,
                   content: str, author: str, data: datetime):
    ''' Обновление news'''
    new = News.get(News.id == new_id)
    new.heading = heading
    new.content = content
    new.author = author
    new.data = data
    new.save()
    return {
        'id': new.id,
        'heading': new.heading,
        'content': new.content,
        'author': new.author,
        'data': new.data
    }


def update_comment_db(com_id: int, news: str,
                      author: str, content: str, data: datetime):
    ''' Обновление comment'''
    com = Comments.get(Comments.id == com_id)
    com.news = news
    com.author = author
    com.content = content
    com.data = data
    com.save()
    return {
        'id': com.id,
        'news': com.news,
        'author': com.author,
        'content': com.content,
        'data': com.data
    }


# Запросы на удаление

def delete_users_db(user_id: int):
    ''' удаление users'''
    user = Users.get(Users.id == user_id)
    user.delete_instance()


def delete_roles_db(rol_id: int):
    ''' удаление roles'''
    rol = Roles.get(Roles.id == rol_id)
    rol.delete_instance()


def delete_news_db(new_id: int):
    ''' удаление news'''
    new = News.get(News.id == new_id)
    new.delete_instance()


def delete_comment_db(com_id: int):
    ''' удаление comment'''
    com = Comments.get(Comments.id == com_id)
    com.delete_instance()


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


# Методы обновления

@app.put('/users/{user_id}')
def update_user(user_id: int, role_id: int, username: str, password: str):
    ''' Обновление пользователя '''
    return update_users_db(user_id, role_id, username, password)


@app.put('/roles/{rol_id}')
def update_roles(rol_id: int, name: str):
    ''' обновление roles'''
    return update_roles_db(rol_id, name)


@app.put('/news/{new_id}')
def update_news(new_id: int, heading: str,
                content: str, author: str, data: datetime):
    ''' Обновление news'''
    return update_news_db(new_id, heading, content, author, data)


@app.put('/comment/{com_id}')
def update_comment(com_id: int, news: str,
                   author: str, content: str, data: datetime):
    ''' Обновление comment'''
    return update_comment_db(com_id, news, author, content, data)

# методы удаления


@app.delete('/del_users/{user_id}')
def delete_users(user_id: int):
    ''' удаление users'''
    return delete_users_db(user_id)


@app.delete('/del_roles/{rol_id}')
def delete_roles(rol_id: int):
    ''' удаление roles'''
    return delete_roles_db(rol_id)


@app.delete('/del_news/{new_id}')
def delete_news(new_id: int):
    ''' удааление news'''
    return delete_news_db(new_id)


@app.delete('/del_comment/{com_id}')
def delete_comment(com_id: int):
    ''' удаление comment'''
    return delete_comment_db(com_id)


db.connect()
db.close()
