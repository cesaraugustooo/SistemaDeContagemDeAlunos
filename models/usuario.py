from peewee import CharField, AnyField, Model, AutoField

from config.database import database


class UsuarioDb(Model):
    id = AutoField(primary_key=True)
    nif = CharField()
    nome = CharField()
    email = CharField()
    senha = CharField()
    foto = CharField()

    class Meta:
        database = database

