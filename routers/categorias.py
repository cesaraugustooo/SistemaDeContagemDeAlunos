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

@router.delete(path='', response_model=CategoriaRead)
def delete_categoria(id : int):
    categoria = Categoria.get_or_none(id == Categoria.id)
    categoria.delete_instance()
    return categoria


@router.get(path='/{ }', response_model=CategoriaRead)
def listar_categoria_id(id: int):
    categoria = Categoria.get_or_none(id == Categoria.id)
    return categoria
