from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=schemas.UsuarioResponse)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.obtener_usuario_por_nombre(db, usuario.usuario)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    return crud.crear_usuario(db, usuario)

@router.post("/login", response_model=schemas.UsuarioResponse)
def login(usuario: schemas.UsuarioLogin, db: Session = Depends(get_db)):
    db_usuario = crud.obtener_usuario_por_nombre(db, usuario.usuario)
    if not db_usuario or db_usuario.contraseña != usuario.contraseña:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return db_usuario


@router.get("/{id_usuario}/historial", response_model=list[schemas.HistorialIntentoResponse])
def historial_usuario(id_usuario: int, db: Session = Depends(get_db)):
    return crud.obtener_historial_por_usuario(db, id_usuario)