from peewee import AutoField,CharField,Model
from config.database import database

class TiposDB(Model):
    id = AutoField()
    nome_tipo = CharField()

    class Meta:
        database = database