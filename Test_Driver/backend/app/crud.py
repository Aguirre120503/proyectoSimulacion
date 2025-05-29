from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

# ========== Usuarios ==========
def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        apellido_paterno=usuario.apellido_paterno,
        apellido_materno=usuario.apellido_materno,
        usuario=usuario.usuario,
        contraseña=usuario.contraseña,
        correo=usuario.correo,
        aprobado=usuario.aprobado,
        rol=usuario.rol
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def obtener_usuario_por_id(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == user_id).first()


def obtener_usuario_por_nombre(db: Session, username: str):
    return db.query(models.Usuario).filter(models.Usuario.usuario == username).first()

# ========== Exámenes ==========
def crear_examen(db: Session, examen: schemas.ExamenCreate):
    db_examen = models.Examen(
        id_usuario=examen.id_usuario,
        tipo_examen=examen.tipo_examen,
        fecha=datetime.now()
    )
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen


def obtener_examen_por_id(db: Session, examen_id: int):
    return db.query(models.Examen).filter(models.Examen.id_examen == examen_id).first()

# ========== Preguntas y Opciones ==========
def obtener_preguntas(db: Session, limit: int = 20):
    return db.query(models.Preguntas).limit(limit).all()


def obtener_opciones_por_pregunta(db: Session, pregunta_id: int):
    return db.query(models.OpcionesRespuesta).filter(
        models.OpcionesRespuesta.id_pregunta == pregunta_id
    ).all()

# ========== Respuestas Usuario ==========
def guardar_respuesta_usuario(db: Session, respuesta: schemas.RespuestaUsuarioBase):
    db_respuesta = models.RespuestasUsuario(**respuesta.dict())
    db.add(db_respuesta)
    db.commit()
    db.refresh(db_respuesta)
    return db_respuesta

def contar_intentos_previos(db: Session, id_usuario: int, tipo_examen: str):
    return db.query(models.HistorialIntentos).filter_by(
        id_usuario=id_usuario,
        tipo_examen=tipo_examen
    ).count()


# ========== Intentos Examen ==========
def registrar_intento(db: Session, intento: schemas.IntentoExamenCreate):
    db_intento = models.IntentosExamen(**intento.dict())
    db.add(db_intento)
    db.commit()
    db.refresh(db_intento)
    return db_intento

# ========== Historial Intentos ==========
def registrar_historial(db: Session, historial: schemas.HistorialIntentoCreate):
    db_historial = models.HistorialIntentos(**historial.dict())
    db.add(db_historial)
    db.commit()
    db.refresh(db_historial)
    return db_historial

# ==========  ==========

def obtener_historial_por_usuario(db: Session, id_usuario: int):
    return db.query(models.HistorialIntentos).filter_by(id_usuario=id_usuario).order_by(models.HistorialIntentos.id_historial.desc()).all()

