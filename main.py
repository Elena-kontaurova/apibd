''' main для fastapi + mysql'''
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form, HTTPException
from peewee import DoesNotExist
from connect import db, Users, Roles, News, Comments, UserUpdate, \
                    NewsUpdate, CommentUpdate, RolesUpdate
from dao.user_dao import UsersDAO
from dao.rol_dao import RolesDAO
from dao.news_dao import NewsDAO
from dao.comment_dao import CommentDAO


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"),
          name="static")
# Методы просмотра


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    ''' Получение всех'''
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
def create_user(request: Request, role_id: int = Form(...),
                username: str = Form(...), password: str = Form(...)):
    ''' Создание новой записи users'''
    UsersDAO.create_user_db(role_id, username, password)
    return templates.TemplateResponse('greate/users_create.html',
                                      {'request': request})


@app.post('/roles_create')
def create_roles(request: Request, name: str = Form(...)):
    ''' Создание новой записи roles'''
    RolesDAO.create_roles_db(name)
    return templates.TemplateResponse('greate/roles_create.html',
                                      {'request': request})


@app.post('/news_create')
def create_news(request: Request, heading: str = Form(...),
                content: str = Form(...), author: str = Form(...),
                data: datetime = Form(...)):
    ''' Создание новой записи news'''
    NewsDAO.create_news_db(heading, content, author, data)
    return templates.TemplateResponse('greate/news_create.html',
                                      {'request': request})


@app.post('/comment_create')
def create_comment(request: Request,
                   news: str = Form(...), author: str = Form(...),
                   content: str = Form(...), data: datetime = Form(...)):
    ''' Создание новой записи comment'''
    CommentDAO.create_comment_db(news, author, content, data)
    return templates.TemplateResponse('greate/comment_create.html',
                                      {'request': request})


# Методы обновления


@app.put('/users/{user_id}')
def update_user(user_id: int, user_data: UserUpdate):
    ''' Обновление пользователя '''
    try:
        user = Users.get(Users.id == user_id)
        user.role_id = user_data.role_id
        user.username = user_data.username
        user.password = user_data.password
        user.save()
        return {"message": "Данные пользователя обновлены"}
    except DoesNotExist as e:
        raise HTTPException(
            status_code=404, detail="Пользователь не найден") from e


@app.put('/roles/{rol_id}')
def update_roles(rol_id: int, rol_data: RolesUpdate):
    ''' обновление roles'''
    try:
        rol = Roles.get(Roles.id == rol_id)
        rol.name = rol_data.name
        rol.save()
        return {"message": "Данные пользователя обновлены"}
    except DoesNotExist as e:
        raise HTTPException(
            status_code=404, detail="Пользователь не найден") from e


@app.put('/news/{new_id}')
def update_news(new_id: int, new_data: NewsUpdate):
    ''' Обновление news'''
    try:
        new = News.get(News.id == new_id)
        new.heading = new_data.heading
        new.content = new_data.content
        new.author = new_data.author
        new.data = new_data.data
        new.save()
        return {'message': "Данные успешно обновленны"}
    except DoesNotExist as e:
        raise HTTPException(
            status_code=404, detail="Пользователь не найден") from e


@app.put('/comment/{com_id}')
def update_comment(com_id: int, com_data: CommentUpdate):
    ''' Обновление comment'''
    com = Comments.get(Comments.id == com_id)
    com.news = com_data.news
    com.author = com_data.author
    com.content = com_data.content
    com.data = com_data.data
    com.save()
    return {'message': 'Данные успешно обновленны'}


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
