from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/respuestas",
    tags=["Respuestas"]
)

@router.post("/", response_model=schemas.RespuestaUsuarioResponse)
def registrar_respuesta(respuesta: schemas.RespuestaUsuarioBase, db: Session = Depends(get_db)):
    return crud.guardar_respuesta_usuario(db, respuesta)
