# 🧭 Simulador de Examen de Manejo - Frontend

Este frontend es una SPA desarrollada en **React + Vite + TailwindCSS**, que permite a los usuarios registrarse, iniciar sesión y realizar un examen teórico de manejo de práctica o final.

---

## 📦 Tecnologías usadas

- React 19
- Vite
- Tailwind CSS
- Axios
- React Router DOM
- Chart.js (con react-chartjs-2)

---

## 🚀 Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/simulador-examen-manejo.git
cd simulador-examen-manejo/frontend
```

### 2. Instala dependencias

```bash
npm install
```

### 3. Inicia el servidor de desarrollo

```bash
npm run dev
```

La app estará disponible en:  
📍 `http://localhost:5173`

---

## 🧠 Funcionalidades

- Registro de nuevos usuarios
- Inicio de sesión
- Simulador de examen con:
  - Examen de práctica (20 preguntas, 5 pts c/u)
  - Examen final (40 preguntas, 2.5 pts c/u)
  - Temporizador por pregunta (60 segundos)
- Evaluación automática y visualización de resultado
- Dashboard con historial de intentos y promedio
- Gráfico de barras comparativo por tipo de examen
- Rutas protegidas para evitar acceso sin login

---

## 📁 Estructura

```
src/
├── api/               # Conexiones al backend
├── components/        # Componentes reutilizables (Timer, PreguntaCard)
├── pages/             # Páginas: Login, Register, Home, Simulador, Resultado,
├── App.jsx            # Enrutamiento general
├── main.jsx           # Punto de entrada principal
└── index.css          # Tailwind config
```

---

## 📌 Notas

- Asegúrate de que el backend esté corriendo en `http://127.0.0.1:8000`
- Las preguntas deben tener imágenes en algunas para visualización óptima.
- Los datos se almacenan y evalúan vía FastAPI con SQLite.
