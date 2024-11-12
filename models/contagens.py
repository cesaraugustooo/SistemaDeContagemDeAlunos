from peewee import AutoField,CharField,Model,DateField,TimeField,IntegerField,ForeignKeyField
from models.usuario import UsuarioDb
from models.turmas import Categoria
from config.database import database


class ContagensDB(Model):
    id = AutoField()
    data = DateField()
    hora = TimeField()
    qtd_contagem = IntegerField()
    usuario = ForeignKeyField(model=UsuarioDb, backref='usuarios')
    categoria = ForeignKeyField(model=Categoria, backref='categoria')

    class Meta:
        database = database