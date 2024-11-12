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


class CategoriaUpdate(BaseModel):
    nome_categoria:str
  
class TurmaBase(BaseModel):
    ano: int
    nome: str
    categoria_id: int

class TurmaCreate(TurmaBase):
    pass

class TurmaUpdate(BaseModel):
    ano: int | None = None
    nome: str | None = None
    ativo: bool | None = None

class TurmaOut(TurmaBase):
    id: int
    categoria_id: CategoriaRead
    ativo: bool
    class Config:
        orm_mode = True

class TurmaRead(BaseModel):
    id: int
    ano: int | None = None
    nome: str | None = None
    categoria_id: CategoriaRead
    ativo: bool | None = None
