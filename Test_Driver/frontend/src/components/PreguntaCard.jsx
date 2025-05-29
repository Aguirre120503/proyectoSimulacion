function PreguntaCard({ pregunta, opciones, onResponder }) {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6 max-w-4xl mx-auto">
      <h2 className="text-xl font-bold text-slate-800 mb-6 leading-relaxed">{pregunta.descripcion}</h2>

      {pregunta.imagen_url && (
        <div className="mb-6 flex justify-center">
          <img
            src={pregunta.imagen_url || "/placeholder.svg"}
            alt="Pregunta"
            className="max-w-full h-auto rounded-lg shadow-md"
          />
        </div>
      )}

      <ul className="space-y-3">
        {opciones.map((op) => (
          <li key={op.id_opcion}>
            <button
              onClick={() => onResponder(op.inciso)}
              className="w-full text-left p-4 border border-slate-200 rounded-lg hover:bg-slate-50 hover:border-indigo-400 focus:outline-none focus:ring-indigo-600 focus:border-indigo-600 transition duration-150 ease-in-out"
            >
              <span className="font-semibold text-indigo-700 mr-3">{op.inciso}:</span>
              <span className="text-slate-800">{op.descripcion_respuesta}</span>
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default PreguntaCard;
