from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# ========== Usuario ==========
class UsuarioBase(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    usuario: str
    correo: EmailStr
    aprobado: Optional[bool] = False
    rol: Optional[int] = 0


class UsuarioCreate(UsuarioBase):
    contraseña: str

class UsuarioLogin(BaseModel):
    usuario: str
    contraseña: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        orm_mode = True

# ========== Examen ==========
class ExamenBase(BaseModel):
    tipo_examen: str


class ExamenCreate(ExamenBase):
    id_usuario: int


class ExamenResponse(ExamenBase):
    id_examen: int
    id_usuario: int
    fecha: datetime
    calificacion: Optional[float]
    resultado: Optional[bool]

    class Config:
        orm_mode = True

# ========== Preguntas y Respuestas ==========
class PreguntaBase(BaseModel):
    descripcion: str
    imagen_url: Optional[str] = None


class OpcionRespuestaBase(BaseModel):
    descripcion_respuesta: str
    correcta: bool
    inciso: str


class OpcionRespuestaCreate(OpcionRespuestaBase):
    id_pregunta: int


class OpcionRespuestaResponse(OpcionRespuestaBase):
    id_opcion: int
    id_pregunta: int
    descripcion_respuesta: str
    correcta: bool
    inciso: str

    class Config:
        orm_mode = True


class RespuestaUsuarioBase(BaseModel):
    id_examen: int
    id_pregunta: int
    respuesta_usuario: str
    valor_respuesta: str


class RespuestaUsuarioResponse(RespuestaUsuarioBase):
    id_respuesta: int

    class Config:
        orm_mode = True

class RespuestaUsuarioSimulador(BaseModel):
    id_pregunta: int
    respuesta_usuario: str  # Por ejemplo "B"

class EvaluacionSimuladorRequest(BaseModel):
    id_usuario: int
    tipo_examen: str  # "P" para práctica, "F" para final
    respuestas: List[RespuestaUsuarioSimulador]


class PreguntaResponse(PreguntaBase):
    id_pregunta: int
    opciones: list[OpcionRespuestaResponse]

    class Config:
        orm_mode = True

# ========== Intentos ==========
class IntentoExamenBase(BaseModel):
    tipo_examen: str
    intentos_prueba: int
    intentos_real: int


class IntentoExamenCreate(IntentoExamenBase):
    id_usuario: int


class IntentoExamenResponse(IntentoExamenBase):
    id_intento: int
    id_usuario: int

    class Config:
        orm_mode = True

# ========== Historial ==========
class HistorialIntentoBase(BaseModel):
    tipo_examen: str
    intento_numero: int
    calificacion: float
    resultado: bool


class HistorialIntentoCreate(HistorialIntentoBase):
    id_usuario: int
    id_examen: int


class HistorialIntentoResponse(HistorialIntentoBase):
    id_historial: int
    id_usuario: int
    id_examen: int

    class Config:
        orm_mode = True
