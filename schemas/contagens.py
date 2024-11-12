from pydantic import BaseModel
from schemas.categoria import CategoriaRead
from schemas.usuario import UsuarioRead
from datetime import datetime, time


class ContagemCreate(BaseModel):
    data : datetime
    hora : time
    qtd_contagem : int
    usuario : int
    categoria : int

class ContagemRead(BaseModel):
    id : int
    data : datetime
    hora : time
    qtd_contagem : int
    usuario : UsuarioRead
    categoria : CategoriaRead

class ContagemUpdate(BaseModel):
    qtd_contagem : int
 

class ContagemReadAll(BaseModel):
    contagens : list[ContagemRead]