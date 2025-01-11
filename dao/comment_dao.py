''' comment_dao'''
from datetime import datetime
from connect import Comments


class CommentDAO():
    ''' класс comment dao'''
    @staticmethod
    def get_all_comment_db():
        ''' Получение всех comments'''
        com = Comments.select()
        return [{'id': comm.id, 'news': comm.news, 'author': comm.author,
                'content': comm.content, 'data': comm.data}
                for comm in com]

    @staticmethod
    def create_comment_db(news: str, author: str,
                          content: str, data: datetime):
        ''' Создание записи comment'''
        com = Comments.create(news=news, author=author,
                              content=content, data=data)
        return {
            'news': com.news,
            'author': com.author,
            'content': com.content,
            'data': com.data
        }

    @staticmethod
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

    @staticmethod
    def delete_comment_db(com_id: int):
        ''' удаление comment'''
        com = Comments.get(Comments.id == com_id)
        com.delete_instance()
