''' main для fastapi + mysql'''
from datetime import datetime
from fastapi import FastAPI
from connect import db
from dao.user_dao import UsersDAO
from dao.rol_dao import RolesDAO
from dao.news_dao import NewsDAO
from dao.comment_dao import CommentDAO


app = FastAPI()

# Методы просмотра


@app.get('/users')
def get_all_users():
    ''' Получение всех users'''
    return UsersDAO.get_all_users_db()


@app.get('/roles')
def get_all_roles():
    ''' Получение всез roles'''
    return RolesDAO.get_all_roles_db()


@app.get('/news')
def get_all_news():
    ''' получение всех news'''
    return NewsDAO.get_all_news_db()


@app.get('/comment')
def get_all_comment():
    ''' Получение всез comment'''
    return CommentDAO.get_all_comment_db()


# Методы создания


@app.post('/user_create')
def create_user(role_id: int, username: str, password: str):
    ''' Создание новой записи users'''
    return UsersDAO.create_user_db(role_id, username, password)


@app.post('/roles_create')
def create_roles(name: str):
    ''' Создание новой записи roles'''
    return RolesDAO.create_roles_db(name)


@app.post('/news_create')
def create_news(heading: str, content: str, author: str, data: datetime):
    ''' Создание новой записи news'''
    return NewsDAO.create_news_db(heading, content, author, data)


@app.post('/comment_create')
def create_comment(news: str, author: str, content: str, data: datetime):
    ''' Создание новой записи comment'''
    return CommentDAO.create_comment_db(news, author, content, data)


# Методы обновления

@app.put('/users/{user_id}')
def update_user(user_id: int, role_id: int, username: str, password: str):
    ''' Обновление пользователя '''
    return UsersDAO.update_users_db(user_id, role_id, username, password)


@app.put('/roles/{rol_id}')
def update_roles(rol_id: int, name: str):
    ''' обновление roles'''
    return RolesDAO.update_roles_db(rol_id, name)


@app.put('/news/{new_id}')
def update_news(new_id: int, heading: str,
                content: str, author: str, data: datetime):
    ''' Обновление news'''
    return NewsDAO.update_news_db(new_id, heading, content, author, data)


@app.put('/comment/{com_id}')
def update_comment(com_id: int, news: str,
                   author: str, content: str, data: datetime):
    ''' Обновление comment'''
    return CommentDAO.update_comment_db(com_id, news, author, content, data)

# методы удаления


@app.delete('/del_users/{user_id}')
def delete_users(user_id: int):
    ''' удаление users'''
    return UsersDAO.delete_users_db(user_id)


@app.delete('/del_roles/{rol_id}')
def delete_roles(rol_id: int):
    ''' удаление roles'''
    return RolesDAO.delete_roles_db(rol_id)


@app.delete('/del_news/{new_id}')
def delete_news(new_id: int):
    ''' удааление news'''
    return NewsDAO.delete_news_db(new_id)


@app.delete('/del_comment/{com_id}')
def delete_comment(com_id: int):
    ''' удаление comment'''
    return CommentDAO.delete_comment_db(com_id)


db.connect()
db.close()
