from pydantic import BaseModel

class TipoCreate(BaseModel):
    nome_tipo : str

class TipoRead(BaseModel):
    id : int
    nome_tipo : str

class TipoAtualizado(BaseModel):
    nome_tipo : str


class TipoReadAll(BaseModel):
    tipos : list[TipoRead]