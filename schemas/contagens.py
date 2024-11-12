from pydantic import BaseModel
from schemas.categoria import CategoriaRead,TurmaOut
from schemas.usuario import UsuarioRead
from datetime import datetime, time


class ContagemCreate(BaseModel):
    data : datetime
    hora : time
    qtd_contagem : int
    usuario : int
    turma_id : int

class ContagemRead(BaseModel):
    id : int
    data : datetime
    hora : time
    qtd_contagem : int
    usuario : UsuarioRead
    turma_id : TurmaOut

class ContagemUpdate(BaseModel):
    qtd_contagem : int
 

class ContagemReadAll(BaseModel):
    contagens : list[ContagemRead]