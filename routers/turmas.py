from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from schemas.turmas import TurmaCreate, TurmaRead, TurmaReadAll, turma_atualizado
from models.turmas import Turma,Categoria

router = APIRouter(prefix='/turmas', tags=['Turmas'])

@router.get(path='', response_model=TurmaReadAll)
def list_all_turmas():
    turmas = Turma.select()
    return {'turmas': turmas}


@router.post(path="", response_model=TurmaRead)
def create_turma(turmaSchema: TurmaCreate):
    turma = Turma.create(**turmaSchema.model_dump())
    return turma


@router.get(path="/{turma_id}", response_model=TurmaRead)
def list_turmas(turma_id: int):
    turma = Turma.get_or_none(Turma.id == turma_id)
    return turma


@router.delete(path="", response_model=TurmaRead)
def delete_turma(id_turma : int):
    turma_delete = Turma.get_or_none(Turma.id == id_turma)
    if turma_delete:
        turma_delete.delete_instance()
        return turma_delete
    else: 
        return 'Turma nao encontrada'


@router.patch(path="", response_model=TurmaRead)
def update_turma(turma : turma_atualizado):
    update = Turma.get_or_none(Turma.id == turma.id)
    update.nome_turma = turma.nome_turma
    update.id_categorias_turma = turma.id_categorias_turma
    update.save()
    return update