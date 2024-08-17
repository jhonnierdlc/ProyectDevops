from pydantic import BaseModel


class Persona(BaseModel):
    tipo_identificacion: str
    numero_identificacion: int
    nombre1: str
    nombre2: str
    apellido1: str
    apellido2: str
    sexo: str
    fecha_nacimiento: str