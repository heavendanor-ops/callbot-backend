from pydantic import BaseModel

class Transportador(BaseModel):
    nombre: str
    telefono: str | None = None