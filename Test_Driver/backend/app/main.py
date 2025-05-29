from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from app.routers import usuarios
from app.routers import preguntas
from app.routers import examenes
from app.routers import respuestas
from app.routers import simulador

# Crear las tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simulador de Examen de Manejo")

# CORS para permitir frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes limitarlo a http://localhost:5173 si usas Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== ENDPOINT ==========
# Incluir el router de usuarios
app.include_router(usuarios.router)
# Incluir el router de preguntas
app.include_router(preguntas.router)
# Incluir el router de examenes
app.include_router(examenes.router)
# Incluir el router de respuestas
app.include_router(respuestas.router)
# Incluir el router de simulador
app.include_router(simulador.router)
# ==============================

# Dependencia para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
