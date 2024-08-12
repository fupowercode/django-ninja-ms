from pydantic import BaseModel

class UsuarioIn(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    nombre_cuenta: str
    contraseña: str

class UsuarioSchema(UsuarioIn):
    id: int

    class Config:
        from_attributes = True  # Habilita la serialización de objetos ORM