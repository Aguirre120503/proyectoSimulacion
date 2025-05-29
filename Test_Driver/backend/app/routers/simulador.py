from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
import random

router = APIRouter(
    prefix="/simulador",
    tags=["Simulador"]
)

@router.get("/practica")
def obtener_preguntas_practica(db: Session = Depends(get_db)):
    preguntas = crud.obtener_preguntas(db, limit=20)
    random.shuffle(preguntas)
    for p in preguntas:
        p.opciones = crud.obtener_opciones_por_pregunta(db, p.id_pregunta)
    return preguntas

@router.get("/final")
def obtener_preguntas_final(db: Session = Depends(get_db)):
    preguntas = crud.obtener_preguntas(db, limit=40)
    random.shuffle(preguntas)
    for p in preguntas:
        p.opciones = crud.obtener_opciones_por_pregunta(db, p.id_pregunta)
    return preguntas


@router.post("/evaluar")
def evaluar_examen(data: schemas.EvaluacionSimuladorRequest, db: Session = Depends(get_db)):
    # Crear examen
    nuevo_examen = schemas.ExamenCreate(
        id_usuario=data.id_usuario,
        tipo_examen=data.tipo_examen
    )
    examen_db = crud.crear_examen(db, nuevo_examen)
    
    aciertos = 0
    for r in data.respuestas:
        opciones = crud.obtener_opciones_por_pregunta(db, r.id_pregunta)
        correcta = next((op for op in opciones if op.correcta), None)

        valor = correcta.inciso if correcta else ""
        es_correcta = (valor == r.respuesta_usuario)

        # Guardar respuesta
        crud.guardar_respuesta_usuario(db, schemas.RespuestaUsuarioBase(
            id_examen=examen_db.id_examen,
            id_pregunta=r.id_pregunta,
            respuesta_usuario=r.respuesta_usuario,
            valor_respuesta=valor
        ))

        if es_correcta:
            aciertos += 1

    total = len(data.respuestas)
    porcentaje = round((aciertos / total) * 100, 2)
    aprobado = porcentaje >= 75.0

    # Actualizar examen con calificación
    examen_db.calificacion = porcentaje
    examen_db.resultado = aprobado
    db.commit()

    # Registrar historial intento
    intento_num = crud.contar_intentos_previos(db, data.id_usuario, data.tipo_examen)
    historial = schemas.HistorialIntentoCreate(
        id_usuario=data.id_usuario,
        id_examen=examen_db.id_examen,
        tipo_examen=data.tipo_examen,
        intento_numero=intento_num + 1,
        calificacion=porcentaje,
        resultado=aprobado
    )
    crud.registrar_historial(db, historial)

    return {
        "aciertos": aciertos,
        "total": total,
        "calificacion": porcentaje,
        "aprobado": aprobado
    }