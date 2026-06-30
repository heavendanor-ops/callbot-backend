from fastapi import APIRouter
from schemas.transportador import Transportador   # ya está bien, déjalo así

router = APIRouter()

@router.post("/call")
def hacer_llamada(data: Transportador):
    respuesta = {
        "mensaje": f"Llamada procesada para {data.nombre}",
        "estado": "ok"
    }
    return respuesta