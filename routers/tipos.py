from fastapi import APIRouter
from schemas.tipos import TipoAtualizado,TipoCreate,TipoRead,TipoReadAll
from models.tipos import TiposDB

router = APIRouter(prefix="/tipos", tags=['Tipos'])



@router.post(path='',response_model=TipoRead)
def criar_tipo(tipos : TipoCreate):
    criar = TiposDB.create(**tipos.model_dump())
    return criar


@router.get(path='',response_model=TipoReadAll)
def list_all_tipos():
    tipos = TiposDB.select()
    return {'tipos':tipos}


@router.get(path='/{id}',response_model=TipoRead)
def list_tipos(id : int):
    tipos = TiposDB.get_or_none(TiposDB.id == id)

    return tipos


@router.delete(path='',response_model=TipoRead)
def list_tipos(id : int):
    tipos = TiposDB.get_or_none(TiposDB.id == id)
    tipos.delete_instance()
    return tipos

@router.patch(path='',response_model=TipoRead)
def update_tipos(id : int, update : TipoAtualizado):
    tipos = TiposDB.get_or_none(TiposDB.id == id)
    tipos.nome_tipo = update.nome_tipo

    tipos.save()
    return tipos