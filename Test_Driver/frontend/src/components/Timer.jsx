"use client"

import { useEffect, useState } from "react"

function Timer({ tiempo = 60, onTiempoTerminado }) {
  const [segundos, setSegundos] = useState(tiempo)

  useEffect(() => {
    if (segundos <= 0) {
      onTiempoTerminado()
      return
    }

    const intervalo = setInterval(() => {
      setSegundos((prev) => prev - 1)
    }, 1000)

    return () => clearInterval(intervalo)
  }, [segundos])

  // Calcular el porcentaje de tiempo restante para la barra de progreso
  const porcentajeRestante = (segundos / tiempo) * 100

  // Determinar el color basado en el tiempo restante
  const getColorClasses = () => {
    if (segundos <= 10) {
      return "bg-red-100 border-red-300 text-red-800"
    } else if (segundos <= 20) {
      return "bg-yellow-100 border-yellow-300 text-yellow-800"
    } else {
      return "bg-slate-50 border-slate-300 text-slate-700"
    }
  }

  const getProgressColor = () => {
    if (segundos <= 10) {
      return "bg-red-500"
    } else if (segundos <= 20) {
      return "bg-yellow-500"
    } else {
      return "bg-indigo-700"
    }
  }

  return (
    <div className="mb-6">
      <div className={`rounded-lg border-2 p-4 transition-all duration-300 ${getColorClasses()}`}>
        <div className="flex items-center justify-between mb-3">
          <span className="text-sm font-semibold">Tiempo restante</span>
          <span className="text-2xl font-bold tabular-nums">
            {Math.floor(segundos / 60)}:{(segundos % 60).toString().padStart(2, "0")}
          </span>
        </div>

        {/* Barra de progreso del tiempo */}
        <div className="w-full bg-slate-200 rounded-full h-2">
          <div
            className={`h-2 rounded-full transition-all duration-1000 ease-linear ${getProgressColor()}`}
            style={{ width: `${porcentajeRestante}%` }}
          ></div>
        </div>

        {/* Indicador visual cuando queda poco tiempo */}
        {segundos <= 10 && <div className="mt-2 text-xs font-medium animate-pulse">⚠️ ¡Tiempo casi agotado!</div>}
      </div>
    </div>
  )
}

export default Timer
