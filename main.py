''' main для fastapi + mysql'''
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form
from connect import db
from dao.user_dao import UsersDAO
from dao.rol_dao import RolesDAO
from dao.news_dao import NewsDAO
from dao.comment_dao import CommentDAO


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Методы просмотра


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    ''' Получение всех users'''
    return templates.TemplateResponse("main.html", {'request': request})


@app.get('/users', response_class=HTMLResponse)
async def get_all_users(request: Request):
    ''' Получение всех users'''
    users = UsersDAO.get_all_users_db()
    return templates.TemplateResponse("users.html", {"request": request,
                                                     "users": users})


@app.get('/roles', response_class=HTMLResponse)
async def get_all_roles(request: Request):
    ''' Получение всез roles'''
    rol = RolesDAO.get_all_roles_db()
    return templates.TemplateResponse('roles.html', {"request": request,
                                                     'role': rol})


@app.get('/news', response_class=HTMLResponse)
async def get_all_news(request: Request):
    ''' получение всех news'''
    ne = NewsDAO.get_all_news_db()
    return templates.TemplateResponse('news.html', {'request': request,
                                                    'new': ne})


@app.get('/comment', response_class=HTMLResponse)
def get_all_comment(request: Request):
    ''' Получение всез comment'''
    comm = CommentDAO.get_all_comment_db()
    return templates.TemplateResponse('comment.html', {'request': request,
                                                       'com': comm})


# Методы создания


@app.post('/user_create')
def create_user(role_id: int = Form(...), username: str = Form(...),
                password: str = Form(...)):
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
