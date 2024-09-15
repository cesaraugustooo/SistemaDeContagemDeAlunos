from fastapi import APIRouter
from schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioReadAll, usuario_atualizado
from models.usuario import UsuarioDb
from fastapi.responses import HTMLResponse


router = APIRouter(prefix='/usuarios', tags=['Usuarios'])


@router.get(path="/usuarios", response_model=UsuarioReadAll)
def listar_usuarios():
    usuarios = UsuarioDb.select()
    return {'usuarios':usuarios}




@router.get(path="/usuarios/{id_usuario}",response_model=UsuarioRead)
def listar_usuarios(id_usuario: int):
    usuario= UsuarioDb.get_or_none(UsuarioDb.id == id_usuario)
    return usuario



@router.post(path="/usuarios/postar", response_model=UsuarioRead)
def postar_usuario(novo_usuario: UsuarioCreate):
    postar = UsuarioDb.create(**novo_usuario.model_dump())

    return postar



@router.delete(path="/usuarios/delete", response_model=UsuarioRead)
def deletar_usuario(id_usuario: int):
    delete = UsuarioDb.get_or_none(UsuarioDb.id == id_usuario)

    delete.delete_instance()

    return delete



@router.patch(path="/usuarios/l{id_usuario}", response_model=UsuarioRead)
def atualizar_usuario(id_usuario, usuario_atualizado:usuario_atualizado):
    usuario = UsuarioDb.get_or_none(UsuarioDb.id == id_usuario)

    usuario.nif = usuario_atualizado.nif
    usuario.nome = usuario_atualizado.nome
    usuario.email = usuario_atualizado.email
    usuario.senha = usuario_atualizado.senha
    usuario.foto = usuario_atualizado.foto

    usuario.save()


    return usuario

