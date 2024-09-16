from peewee import CharField, Model, AutoField, ForeignKeyField
from config.database import database

class Categoria(Model):
    id = AutoField()
    nome_categoria = CharField()
    class Meta:
        database = database


class Turma(Model):
    id = AutoField()
    nome_turma = CharField()
    id_categorias_turma = ForeignKeyField(Categoria, backref='categorias')

    class Meta:
        database = database

