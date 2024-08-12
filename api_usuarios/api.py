from ninja import NinjaAPI
from sitio_usuarios.models import Usuario
from sitio_usuarios.schemas import UsuarioSchema, UsuarioIn
from django.shortcuts import get_object_or_404


api = NinjaAPI()

@api.post("/usuarios/")
def create_usuario(request, payload: UsuarioIn):
    usuario = Usuario.objects.create(**payload.dict())
    return {"success": True, "usuario_id": usuario.id}

@api.get("/usuarios/")
def list_usuarios(request):
    usuarios = Usuario.objects.all()
    return [UsuarioSchema.from_orm(usuario) for usuario in usuarios]

@api.put("/usuarios/{usuario_id}/")
def update_usuario(request, usuario_id: int, payload: UsuarioIn):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in payload.dict().items():
        setattr(usuario, attr, value)
    usuario.save()
    return {"success": True}

@api.delete("/usuarios/{usuario_id}/")
def delete_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}
