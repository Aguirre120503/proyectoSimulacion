import { useState, useEffect } from "react"
import { getPreguntas, evaluarExamen } from "../api/simulador"
import PreguntaCard from "../components/PreguntaCard"
import { useNavigate } from "react-router-dom"
import Timer from "../components/Timer"

function Simulador({ tipo = "P", idUsuario = 1 }) {
  const [preguntas, setPreguntas] = useState([])
  const [respuestas, setRespuestas] = useState([])
  const [index, setIndex] = useState(0)
  const navigate = useNavigate()

  useEffect(() => {
    getPreguntas(tipo).then((res) => setPreguntas(res.data))
  }, [])

  const handleResponder = (inciso) => {
    const pregunta = preguntas[index]
    setRespuestas([...respuestas, { id_pregunta: pregunta.id_pregunta, respuesta_usuario: inciso }])
    setIndex(index + 1)
  }

  const terminarExamen = async () => {
    const resultado = await evaluarExamen({
      id_usuario: idUsuario,
      tipo_examen: tipo,
      respuestas: respuestas,
    })
    navigate("/resultado", { state: resultado.data })
  }

  const onTiempoTerminado = () => {
    terminarExamen()
  }

  if (!preguntas.length)
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-100">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-indigo-700 mx-auto"></div>
          <p className="mt-4 text-lg text-slate-600">Cargando preguntas...</p>
        </div>
      </div>
    )

  if (index >= preguntas.length)
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-100">
        <div className="bg-white p-8 rounded-lg shadow-md text-center max-w-md w-full mx-4">
          <h2 className="text-2xl font-bold text-slate-800 mb-6">Examen terminado</h2>
          <button
            onClick={terminarExamen}
            className="w-full py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-700 hover:bg-indigo-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 transition duration-150 ease-in-out"
          >
            Ver resultado
          </button>
        </div>
      </div>
    )

  const preguntaActual = preguntas[index]

  return (
    <div className="min-h-screen bg-slate-100 py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <div className="mb-6">
          <div className="bg-white rounded-lg shadow-sm p-4">
            <div className="flex justify-between items-center">
              <span className="text-sm font-medium text-slate-600">
                Pregunta {index + 1} de {preguntas.length}
              </span>
              <div className="w-48 bg-slate-300 rounded-full h-2">
                <div
                  className="bg-indigo-700 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${((index + 1) / preguntas.length) * 100}%` }}
                ></div>
              </div>
            </div>
          </div>
        </div>
        <Timer key={index} onTiempoTerminado={onTiempoTerminado} />
        <PreguntaCard
          pregunta={preguntaActual}
          opciones={preguntaActual.opciones || []}
          onResponder={handleResponder}
        />
      </div>
    </div>
  )
}

export default Simulador
