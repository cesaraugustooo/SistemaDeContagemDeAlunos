from fastapi import APIRouter,HTTPException
from schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioReadAll, usuario_atualizado
from models.usuario import UsuarioDb
from fastapi.responses import HTMLResponse


router = APIRouter(prefix='/usuarios', tags=['Usuarios'])


@router.get(path="", response_model=UsuarioReadAll)
def listar_usuarios():
    usuarios = UsuarioDb.select()
    return {'usuarios':usuarios}




@router.get(path="/{id_usuario}",response_model=UsuarioRead)
def listar_usuarios(id_usuario: int):
    usuario= UsuarioDb.get_or_none(UsuarioDb.id == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    return usuario



@router.post(path="", response_model=UsuarioRead)
def postar_usuario(novo_usuario: UsuarioCreate):
    postar = UsuarioDb.create(**novo_usuario.model_dump())

    return postar



@router.delete(path="/delete", response_model=UsuarioRead)
def deletar_usuario(id_usuario: int):
    delete = UsuarioDb.get_or_none(UsuarioDb.id == id_usuario)
    if not delete:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    delete.delete_instance()

    return delete



@router.patch(path="{id_usuario}", response_model=UsuarioRead)
def atualizar_usuario(id_usuario, usuario_atualizado:usuario_atualizado):
    usuario = UsuarioDb.get_or_none(UsuarioDb.id == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    usuario.nif = usuario_atualizado.nif
    usuario.nome = usuario_atualizado.nome
    usuario.email = usuario_atualizado.email
    usuario.senha = usuario_atualizado.senha
    usuario.foto = usuario_atualizado.foto

    usuario.save()


    return usuario

