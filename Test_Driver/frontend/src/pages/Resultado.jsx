import { useLocation, useNavigate } from 'react-router-dom';

function Resultado() {
  const { state } = useLocation();
  const navigate = useNavigate();

  if (!state) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-100">
        <div className="bg-white p-8 rounded-lg shadow-md text-center max-w-md w-full mx-4">
          <h2 className="text-2xl font-bold text-slate-800 mb-6">No hay resultados disponibles</h2>
          <button
            onClick={() => navigate("/home")}
            className="w-full py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-700 hover:bg-indigo-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 transition duration-150 ease-in-out"
          >
            Volver al inicio
          </button>
        </div>
      </div>
    )
  }

  const { aciertos, total, calificacion, aprobado } = state;

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full">
        <div className="bg-white rounded-lg shadow-lg p-8 text-center">
          <h1 className="text-3xl font-bold text-slate-800 mb-8">Resultado del Examen</h1>

          <div className="space-y-4 mb-8">
            <div className="bg-slate-50 rounded-lg p-4">
              <p className="text-lg text-slate-700">
                <span className="font-semibold">Preguntas respondidas:</span> {total}
              </p>
            </div>

            <div className="bg-slate-50 rounded-lg p-4">
              <p className="text-lg text-slate-700">
                <span className="font-semibold">Aciertos:</span> {aciertos}
              </p>
            </div>

            <div className="bg-slate-50 rounded-lg p-4">
              <p className="text-lg text-slate-700">
                <span className="font-semibold">Calificación:</span> {calificacion}%
              </p>
            </div>
          </div>

          <div className={`p-6 rounded-lg mb-8 ${aprobado ? "bg-cyan-100" : "bg-blue-100"}`}>
            <h2 className={`text-2xl font-bold ${aprobado ? "text-cyan-800" : "text-blue-800"}`}>
              {aprobado ? "¡Aprobado!" : "No aprobado"}
            </h2>
          </div>

          <button
            onClick={() => navigate("/home")}
            className="w-full py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-700 hover:bg-indigo-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 transition duration-150 ease-in-out"
          >
            Volver al inicio
          </button>
        </div>
      </div>
    </div>
  )
}

export default Resultado;
