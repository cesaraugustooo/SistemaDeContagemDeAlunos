from peewee import CharField, Model, AutoField, ForeignKeyField,DateField,BooleanField
from config.database import database

class Categoria(Model):
    id = AutoField()
    nome_categoria = CharField()
    class Meta:
        database = database



class Turma(Model):
    id = AutoField()
    ano = DateField()
    nome = CharField()
    categoria_id = ForeignKeyField(Categoria, backref='turmas')
    ativo = BooleanField(default=True)
    
    class Meta:
        database = database