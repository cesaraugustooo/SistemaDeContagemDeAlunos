from fastapi import APIRouter
from schemas.categoria import CategoriaSchemaCreate,CategoriaSchema,CategoriaRead,CategoriaList
from config.database import conect,end_database
from models.turmas import Categoria
from fastapi.responses import HTMLResponse
router = APIRouter(prefix='/categoria', tags=['Categorias'])



@router.post(path="", response_model=CategoriaRead)
def create_turma(categoria: CategoriaSchemaCreate):
    create_categoria = Categoria.create(**categoria.model_dump())

    return create_categoria


@router.get(path='', response_model=CategoriaList)
def listar_categoria():
    categorias = Categoria.select()
    return  {'categorias':categorias}



