from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nif: str
    nome: str
    email: str
    senha: str
    foto: str

class UsuarioRead(BaseModel):
    id: int
    nif: str
    nome: str
    email: str
    foto: str

class usuario_atualizado(BaseModel):
    nif: str
    nome: str
    email: str
    senha: str

class UsuarioReadAll(BaseModel):
    usuarios: list[UsuarioRead]