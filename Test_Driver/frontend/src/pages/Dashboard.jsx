import { useEffect, useState } from 'react';
import { getHistorial } from '../api/simulador';
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

function Dashboard({ usuario }) {
  const [historial, setHistorial] = useState([]);
  const [promedios, setPromedios] = useState({ practica: 0, final: 0 });

  useEffect(() => {
    if (usuario) {
      getHistorial(usuario.id_usuario).then((res) => {
        setHistorial(res.data);
        calcularPromedios(res.data);
      });
    }
  }, [usuario]);

  const calcularPromedios = (datos) => {
    const practicas = datos.filter(h => h.tipo_examen === 'P');
    const finales = datos.filter(h => h.tipo_examen === 'F');

    const avg = arr => arr.length ? arr.reduce((a, b) => a + b.calificacion, 0) / arr.length : 0;

    setPromedios({
      practica: Math.round(avg(practicas)),
      final: Math.round(avg(finales)),
    });
  };

  const data = {
    labels: ['Práctica', 'Final'],
    datasets: [{
      label: 'Promedio (%)',
      data: [promedios.practica, promedios.final],
      backgroundColor: ['#4F46E5', '#0EA5E9']
    }]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: { enabled: true }
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 100
      }
    }
  };

  return (
    <div className="min-h-screen bg-slate-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto bg-white shadow-md rounded-lg p-8">
        <h2 className="text-2xl font-bold text-slate-800 mb-6 text-center">Dashboard de Exámenes</h2>

        <div className="mb-10">
          <Bar data={data} options={options} />
        </div>

        <table className="min-w-full divide-y divide-slate-200">
          <thead className="bg-slate-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-slate-600 uppercase">Intento</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-slate-600 uppercase">Tipo</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-slate-600 uppercase">Calificación</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-slate-600 uppercase">Resultado</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-slate-200">
            {historial.map((h) => (
              <tr key={h.id_historial}>
                <td className="px-6 py-4 text-slate-700">{h.intento_numero}</td>
                <td className="px-6 py-4 text-slate-700">{h.tipo_examen === 'P' ? 'Práctica' : 'Final'}</td>
                <td className="px-6 py-4 text-slate-700">{h.calificacion}%</td>
                <td className="px-6 py-4">
                  <span className={`inline-block px-2 py-1 text-xs rounded-full font-semibold ${h.resultado ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                    {h.resultado ? 'Aprobado' : 'No aprobado'}
                  </span>
                </td>
              </tr>
            ))}
            {historial.length === 0 && (
              <tr>
                <td colSpan="4" className="text-center py-6 text-slate-500">No hay intentos registrados.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Dashboard;
