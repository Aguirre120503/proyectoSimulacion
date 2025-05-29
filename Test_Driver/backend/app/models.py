from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Numeric, CHAR
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    apellido_paterno = Column(String(255))
    apellido_materno = Column(String(255))
    usuario = Column(String(20), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    correo = Column(String(255), unique=True)
    aprobado = Column(Boolean, default=False)
    rol = Column(Integer)

    examenes = relationship("Examen", back_populates="usuario")
    historial_intentos = relationship("HistorialIntentos", back_populates="usuario")
    intentos_examen = relationship("IntentosExamen", back_populates="usuario")


class IntentosExamen(Base):
    __tablename__ = "intentos_examen"

    id_intento = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    tipo_examen = Column(CHAR(1))
    intentos_prueba = Column(Integer)
    intentos_real = Column(Integer)

    usuario = relationship("Usuario", back_populates="intentos_examen")


class Examen(Base):
    __tablename__ = "examen"

    id_examen = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    tipo_examen = Column(CHAR(1))
    fecha = Column(DateTime)
    calificacion = Column(Numeric)
    resultado = Column(Boolean)

    usuario = relationship("Usuario", back_populates="examenes")
    respuestas = relationship("RespuestasUsuario", back_populates="examen")


class HistorialIntentos(Base):
    __tablename__ = "historial_intentos"

    id_historial = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_examen = Column(Integer, ForeignKey("examen.id_examen"))
    tipo_examen = Column(CHAR(1))
    intento_numero = Column(Integer)
    calificacion = Column(Numeric)
    resultado = Column(Boolean)

    usuario = relationship("Usuario", back_populates="historial_intentos")


class Preguntas(Base):
    __tablename__ = "preguntas"

    id_pregunta = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255))
    imagen_url = Column(String, nullable=True)

    opciones = relationship("OpcionesRespuesta", back_populates="pregunta")
    respuestas = relationship("RespuestasUsuario", back_populates="pregunta")


class OpcionesRespuesta(Base):
    __tablename__ = "opciones_respuesta"

    id_opcion = Column(Integer, primary_key=True, index=True)
    id_pregunta = Column(Integer, ForeignKey("preguntas.id_pregunta"))
    descripcion_respuesta = Column(String(255))
    correcta = Column(Boolean)
    inciso = Column(CHAR(1))

    pregunta = relationship("Preguntas", back_populates="opciones")


class RespuestasUsuario(Base):
    __tablename__ = "respuestas_usuario"

    id_respuesta = Column(Integer, primary_key=True, index=True)
    id_examen = Column(Integer, ForeignKey("examen.id_examen"))
    id_pregunta = Column(Integer, ForeignKey("preguntas.id_pregunta"))
    respuesta_usuario = Column(CHAR(1))
    valor_respuesta = Column(CHAR(1))

    examen = relationship("Examen", back_populates="respuestas")
    pregunta = relationship("Preguntas", back_populates="respuestas")
