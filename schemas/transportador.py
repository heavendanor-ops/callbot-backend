from pydantic import BaseModel

class Transportador(BaseModel):
    id: int
    nombre: str
    telefono: str