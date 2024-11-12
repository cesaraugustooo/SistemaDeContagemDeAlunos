from peewee import CharField, Model, AutoField, ForeignKeyField
from config.database import database

class Categoria(Model):
    id = AutoField()
    nome_categoria = CharField()
    class Meta:
        database = database



