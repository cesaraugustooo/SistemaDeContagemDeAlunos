from fastapi import APIRouter
from schemas.contagens import ContagemCreate,ContagemRead,ContagemReadAll,ContagemUpdate
from models.contagens import ContagensDB


router = APIRouter(prefix='/Contagens', tags=['Contagens'] )

@router.post(path='',response_model=ContagemRead)
def criar_contagens(contagem : ContagemCreate):
    Contagem = ContagensDB.create(**contagem.model_dump())
    return Contagem

@router.get(path='/{id}',response_model=ContagemRead)
def list_contagens(id : int):
    contagens = ContagensDB.get_or_none(ContagensDB.id == id)
    return contagens

@router.get(path='',response_model=ContagemReadAll)
def list_all_contagens():
    contagens = ContagensDB.select()
    return {'contagens':contagens}

@router.patch(path='',response_model=ContagemRead)
def list_contagens(id : int, con : ContagemUpdate):

    

    contagens = ContagensDB.get_or_none(ContagensDB.id == id)
    contagens.data = con.data
    contagens.hora = con.hora
    contagens.qtd_contagem = con.qtd_contagem
    contagens.tipo = con.tipo
    contagens.usuario = con.usuario
    contagens.turma = con.turma

    contagens.save()

    return contagens