from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/examenes",
    tags=["Examenes"]
)

@router.post("/", response_model=schemas.ExamenResponse)
def crear_examen(examen: schemas.ExamenCreate, db: Session = Depends(get_db)):
    return crud.crear_examen(db, examen)

@router.get("/{examen_id}", response_model=schemas.ExamenResponse)
def obtener_examen(examen_id: int, db: Session = Depends(get_db)):
    examen = crud.obtener_examen_por_id(db, examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen
