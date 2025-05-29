from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/preguntas",
    tags=["Preguntas"]
)

@router.get("/", response_model=list[schemas.PreguntaResponse])
def obtener_preguntas(limit: int = 20, db: Session = Depends(get_db)):
    preguntas = crud.obtener_preguntas(db, limit=limit)
    return preguntas


@router.get("/{pregunta_id}/opciones", response_model=list[schemas.OpcionRespuestaResponse])
def obtener_opciones(pregunta_id: int, db: Session = Depends(get_db)):
    opciones = crud.obtener_opciones_por_pregunta(db, pregunta_id)
    print(f"Tipo de ID recibido: {type(pregunta_id)}")
    print(f"Opciones para pregunta {pregunta_id}:", opciones)
    if not opciones:
        raise HTTPException(status_code=404, detail="No se encontraron opciones para esta pregunta")
    return opciones
