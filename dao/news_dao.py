''' news_dao'''
from datetime import datetime
from connect import News


class NewsDAO():
    ''' класс news dao'''
    @staticmethod
    def get_all_news_db():
        ''' Получение всех news'''
        new = News.select()
        return [{'id': ne.id, 'heading': ne.heading, 'content': ne.content,
                'author': ne.author, 'data': ne.data}
                for ne in new]

    @staticmethod
    def create_news_db(heading: str, content: str,
                       author: str, data: datetime):
        ''' Создание записи News'''
        new = News.create(heading=heading, content=content,
                          author=author, data=data)
        return {
            'heading': new.heading,
            'content': new.content,
            'author': new.author,
            'data': new.data
        }

    @staticmethod
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

    @staticmethod
    def delete_news_db(new_id: int):
        ''' удаление news'''
        new = News.get(News.id == new_id)
        new.delete_instance()
