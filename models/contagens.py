from peewee import AutoField,CharField,Model,DateField,TimeField,IntegerField,ForeignKeyField
from models.usuario import UsuarioDb
from models.tipos import TiposDB
from models.turmas import Turma,Categoria
from config.database import database


class ContagensDB(Model):
    id = AutoField()
    data = DateField()
    hora = TimeField()
    qtd_contagem = IntegerField()
    tipo = ForeignKeyField(model=TiposDB, backref='tipos')
    usuario = ForeignKeyField(model=UsuarioDb, backref='usuarios')
    turma = ForeignKeyField(model=Turma, backref='turma')

    class Meta:
        database = database