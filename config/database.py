from peewee import SqliteDatabase

database = SqliteDatabase("database2.db")

def conect():
    database.connect()
    from models.usuario import UsuarioDb
    from models.turmas import Categoria
    from models.tipos import TiposDB
    from models.contagens import ContagensDB
    database.create_tables([UsuarioDb,Turma,Categoria,TiposDB,ContagensDB])

def end_database():
    database.close()