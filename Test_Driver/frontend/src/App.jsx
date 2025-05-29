import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useState } from 'react';
import Login from './pages/Login';
import Register from './pages/Register';
import Home from './pages/Home';
import Simulador from './pages/Simulador';
import Resultado from './pages/Resultado';
import Dashboard from './pages/Dashboard'; // ✅ ¡Importación necesaria!

function App() {
  const [usuario, setUsuario] = useState(null);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login onLogin={setUsuario} />} />
        <Route path="/register" element={<Register onRegister={setUsuario} />} />
        <Route path="/home" element={<Home usuario={usuario} />} />
        <Route path="/simulador" element={<Simulador idUsuario={usuario?.id_usuario} />} />
        <Route path="/resultado" element={<Resultado />} />
        <Route path="/dashboard" element={<Dashboard usuario={usuario} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
