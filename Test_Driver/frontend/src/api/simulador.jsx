import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000', // tu backend
});

// Obtener preguntas aleatorias
export const getPreguntas = (tipo = 'P') =>
  API.get(`/simulador/${tipo === 'F' ? 'final' : 'practica'}`);

// Evaluar respuestas
export const evaluarExamen = (data) =>
  API.post('/simulador/evaluar', data);

// Guardar respuesta individual (opcional si lo haces pregunta por pregunta)
export const guardarRespuesta = (data) =>
  API.post('/respuestas/', data);

export const getHistorial = (idUsuario) =>
  API.get(`/usuarios/${idUsuario}/historial`);