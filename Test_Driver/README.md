# 🚗 Simulador de Examen Teórico de Manejo

Este proyecto es una aplicación completa (frontend + backend) que permite a los usuarios prepararse para el examen teórico de manejo. Ofrece simulaciones de práctica y examen final con evaluación automática, control de intentos y dashboard con resultados.

---

## 📂 Estructura del proyecto

```
TEST_DRIVER/
├── backend/           # API FastAPI + SQLite
│   ├── app/           # Modelos, rutas, lógica de negocio
│   ├── assets/        # SQL para poblar preguntas
│   ├── venv/          # Entorno virtual (ignorado por Git)
│   ├── app.db         # Base de datos SQLite
│   ├── requirements.txt
│   └── README.md
│
├── frontend/          # React + Vite + Tailwind
│   ├── src/           # Componentes, páginas, lógica UI
│   ├── public/
│   ├── package.json
│   └── README.md
│
└── README.md          # Este archivo (documentación general)
```

---

## ⚙️ Requisitos

- Python 3.10+
- Node.js + npm
- SQLite
- Git

---

## 🚀 Cómo ejecutar el proyecto

### 1. Backend

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

📍 Acceso backend: `http://127.0.0.1:8000`
📍 Documentación API: `http://127.0.0.1:8000/docs`

---

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

📍 Acceso frontend: `http://localhost:5173`

---

## 🧠 Funcionalidades principales

- Registro e inicio de sesión de usuarios
- Simulador de examen:
  - Práctica: 20 preguntas (máx. 6 intentos)
  - Final: 40 preguntas (máx. 3 intentos)
  - Evaluación automática (5 pts o 2.5 pts por pregunta)
  - Temporizador de 1 minuto por pregunta
- Resultados y feedback (porcentaje y aprobado/no aprobado)
- Dashboard con historial de intentos y promedios
- Gráficas comparativas usando Chart.js
- Carga aleatoria de preguntas sin repetición

---

## 📌 Créditos

Tecnologías utilizadas: **FastAPI**, **SQLite**, **React**, **TailwindCSS**, **Chart.js**.
