from peewee import AutoField,CharField,Model,DateField,TimeField,IntegerField,ForeignKeyField
from models.usuario import UsuarioDb
from models.turmas import Turma
from config.database import database


class ContagensDB(Model):
    id = AutoField()
    data = DateField()
    hora = TimeField()
    qtd_contagem = IntegerField()
    usuario = ForeignKeyField(model=UsuarioDb, backref='usuarios')
    turma_id = ForeignKeyField(model=Turma, backref='turmas')

    class Meta:
        database = database