from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from datetime import datetime, time

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
    if not contagens:
        raise HTTPException(status_code=404, detail="Contagem nao encontrada")
    return contagens




@router.get(path='',response_model=ContagemReadAll)
def list_all_contagens():
    contagens = ContagensDB.select()
    return {'contagens':contagens}




@router.patch(path='',response_model=ContagemRead)
def list_contagens(id : int, con : ContagemUpdate,):

    contagens = ContagensDB.get_or_none(ContagensDB.id == id)
    if not contagens:
        raise HTTPException(status_code=404, detail="Contagem nao encontrada")
    contagens.qtd_contagem = con.qtd_contagem
    contagens.save()
    return contagens