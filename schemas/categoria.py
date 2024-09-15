from pydantic import BaseModel

class CategoriaSchemaCreate(BaseModel):
    nome_categoria: str


class CategoriaSchema(BaseModel):
    id: int

class CategoriaRead(BaseModel):
    id:int
    nome_categoria:str

class CategoriaList(BaseModel):
    categorias: list[CategoriaRead]