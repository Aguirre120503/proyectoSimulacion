import { useNavigate } from 'react-router-dom';

function Home({ usuario }) {
  const navigate = useNavigate();

  if (!usuario) {
    navigate('/');
    return null;
  }

  return (
    <div className="min-h-screen bg-slate-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <div className="text-center">
            <h2 className="text-3xl font-extrabold text-slate-800 mb-6">¡Hola, {usuario.nombre}!</h2>
            <p className="text-lg text-slate-600 mb-8">¿Quieres iniciar el examen teórico de manejo?</p>
            <button
              onClick={() => navigate("/simulador")}
              className="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-700 hover:bg-indigo-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 transition duration-150 ease-in-out"
            >
              Iniciar simulador
            </button>
            <button
              onClick={() => navigate("/dashboard")}
              className="mt-4 w-full py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-indigo-700 bg-white hover:bg-indigo-50 transition"
            >
              Ver dashboard
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home;
