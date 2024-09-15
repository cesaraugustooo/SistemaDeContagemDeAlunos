from pydantic import BaseModel
from schemas.categoria import CategoriaRead
class TurmaCreate(BaseModel):
    nome_turma : str
    id_categorias_turma : int

    

class TurmaRead(BaseModel):
    id: int
    nome_turma: str
    id_categorias_turma : CategoriaRead

 
class turma_atualizado(BaseModel):
    id: int
    nome_turma: str
    id_categorias_turma : int


class TurmaReadAll(BaseModel):
    turmas: list[TurmaRead]