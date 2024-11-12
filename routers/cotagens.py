from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from datetime import datetime, time

from schemas.contagens import ContagemCreate,ContagemRead,ContagemReadAll,ContagemUpdate
from models.contagens import ContagensDB,UsuarioDb


router = APIRouter(prefix='/contagens', tags=['Contagens'] )

@router.post(path='', response_model=ContagemRead)
def criar_contagens(contagem: ContagemCreate):
    try:
        if not contagem.usuario: 
            raise HTTPException(status_code=400, detail="Usuário não fornecido")
        
        nova_contagem = ContagensDB.create(**contagem.model_dump())  
        return nova_contagem

    except Exception:
        raise HTTPException(status_code=400, detail="Erro ao criar contagem")




@router.get(path='',response_model=ContagemReadAll)
def list_all_contagens():
    contagens = ContagensDB.select()
    return {'contagens':contagens}




@router.put(path='',response_model=ContagemRead)
def list_contagens(id : int, con : ContagemUpdate,):

    contagens = ContagensDB.get_or_none(ContagensDB.id == id)
    if not contagens:
        raise HTTPException(status_code=404, detail="Contagem nao encontrada")
    contagens.qtd_contagem = con.qtd_contagem
    contagens.save()
    return contagens