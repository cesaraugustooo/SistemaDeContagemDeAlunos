from pydantic import BaseModel
from schemas.categoria import CategoriaRead
from schemas.usuario import UsuarioRead
from schemas.tipos import TipoRead
from schemas.turmas import TurmaRead
from datetime import datetime, time


class ContagemCreate(BaseModel):
    data : datetime
    hora : time
    qtd_contagem : int
    tipo : int
    usuario : int
    turma : int

class ContagemRead(BaseModel):
    id : int
    data : datetime
    hora : time
    qtd_contagem : int
    tipo : TipoRead
    usuario : UsuarioRead
    turma : TurmaRead

class ContagemUpdate(BaseModel):
    data : datetime
    hora : time
    qtd_contagem : int
    tipo : int
    usuario : int
    turma : int


class ContagemReadAll(BaseModel):
    contagens : list[ContagemRead]