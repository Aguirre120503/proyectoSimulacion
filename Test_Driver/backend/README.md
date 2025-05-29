# 🚗 Simulador de Examen de Manejo - Backend

Este proyecto es una API REST hecha con **FastAPI + SQLite**, que simula un examen teórico de manejo. Es parte de un sistema más amplio con frontend en React.

## 📦 Tecnologías

- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
- dotenv

## 📁 Estructura del proyecto

```text
Backend/
├── app/
│ ├── main.py # App FastAPI
│ ├── models.py # Tablas
│ ├── crud.py # Lógica de BD
│ ├── schemas.py # Pydantic models
│ ├── database.py # Conexión a SQLite
│ └── routers/ # Rutas separadas por entidad
├── app.db # Base de datos SQLite (ignorada por Git)
├── requirements.txt # Dependencias
├── .gitignore
└── README.md
```

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/simulador-examen-manejo.git
cd simulador-examen-manejo/Backend
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Verifica o crea la base de datos app.db. Si ya tienes una base precargada, colócala en la raíz del backend. O ejecuta:

```bash
python app/create_db.py
```

## 🚀 Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

Luego visita:

📍 http://127.0.0.1:8000/docs → Documentación interactiva Swagger.

## 🔑 Endpoints clave

- POST /usuarios/ → Crear usuario
- GET /preguntas/ → Listar preguntas
- GET /preguntas/{id}/opciones → Ver opciones de una pregunta
- POST /respuestas/ → Guardar respuesta de usuario
- POST /simulador/evaluar → Evaluar un examen y calcular calificación

## ✍️ Notas

- Cada pregunta se evalúa automáticamente.
- La calificación se guarda con historial.
- Se considera aprobado con ≥ 75%.
- Soporta examen de práctica (20) y final (40).

## 🧪 Requisitos

- Python 3.10 o superior
- SQLite
- Git (opcional)
