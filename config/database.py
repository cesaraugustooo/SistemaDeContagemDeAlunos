from peewee import SqliteDatabase

database = SqliteDatabase("database2.db")

def conect():
    database.connect()
    from models.usuario import UsuarioDb
    from models.turmas import Categoria,Turma
    from models.contagens import ContagensDB
    database.create_tables([UsuarioDb,Categoria,ContagensDB,Turma])

def end_database():
    database.close()