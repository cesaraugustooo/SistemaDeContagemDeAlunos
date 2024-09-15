from peewee import SqliteDatabase

database = SqliteDatabase("database2.db")

def conect():
    database.connect()
    from models.usuario import UsuarioDb
    from models.turmas import Turma,Categoria
    database.create_tables([UsuarioDb,Turma,Categoria])

def end_database():
    database.close()