''' user_dao'''
from connect import Users


class UsersDAO:
    ''' класс users dao'''
    @staticmethod
    def get_all_users_db():
        ''' получение всех users'''
        users = Users.select()
        return [{'id': user.id, 'role_id': user.role_id,
                 'username': user.username} for user in users]

    @staticmethod
    def create_user_db(role_id: int, username: str, password: str):
        ''' Создание нового пользователя Users'''
        user = Users.create(role_id=role_id,
                            username=username, password=password)
        return {
            'id': user.id,
            'role_id': user.role_id,
            'username': user.username,
            'password': user.password,
        }

    @staticmethod
    def update_users_db(user_id: int, role_id: int,
                        username: str, password: str):
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

    @staticmethod
    def delete_users_db(user_id: int):
        ''' удаление users'''
        user = Users.get(Users.id == user_id)
        user.delete_instance()
