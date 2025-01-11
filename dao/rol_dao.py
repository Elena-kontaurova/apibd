''' rol_dao'''
from connect import Roles


class RolesDAO():
    ''' класс roles dao'''
    @staticmethod
    def get_all_roles_db():
        ''' Получение всех roles'''
        role = Roles.select()
        return [{'id': ro.id, 'name': ro.name} for ro in role]

    @staticmethod
    def create_roles_db(name: str):
        ''' Создание записи Roles'''
        role = Roles.create(name=name)
        return {
            'id': role.id,
            'name': role.name
        }

    @staticmethod
    def update_roles_db(rol_id: int, name: str):
        ''' Обновление roles'''
        rol = Roles.get(Roles.id == rol_id)
        rol.name = name
        rol.save()
        return {
            'id': rol.id,
            'name': rol.name
        }

    @staticmethod
    def delete_roles_db(rol_id: int):
        ''' удаление roles'''
        rol = Roles.get(Roles.id == rol_id)
        rol.delete_instance()
