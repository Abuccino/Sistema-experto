 /*este frontend se ejecuta desde el directorio sistema-experto-gimnasia  con el comando -> npm run dev */
import React, { useState, useEffect } from "react";
import axios from "axios";

const GimnasiaData = () => {
  const [pregunta, setPregunta] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [finalizado, setFinalizado] = useState(false);
  const [resultado, setResultado] = useState(null);

  const reiniciarConsulta = async () => {
    setPregunta(null);
    setFinalizado(false);
    setResultado(null);
    await cargarJson();
  };

  const cargarJson = async () => {
    setLoading(true);
    try {
      await axios.post("http://127.0.0.1:8000/base/cargar", {
        filename: "gimnasia.json",
      });
      iniciarConsulta();
    } catch (err) {
      setError("Error al cargar el archivo JSON.");
    } finally {
      setLoading(false);
    }
  };

  const iniciarConsulta = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://127.0.0.1:8000/consultar/iniciar");
      const data = response.data;
      if (data.pregunta) {
        setPregunta(data.pregunta);
        setFinalizado(false);
      }
    } catch (err) {
      setError("Error al iniciar la consulta.");
    } finally {
      setLoading(false);
    }
  };

  const cargarPregunta = async (respuesta) => {
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/consultar/responder", {
        response: respuesta, // Envía la respuesta del usuario
      });
      const data = response.data;

      if (data.pregunta) {
        setPregunta(data.pregunta);
        setFinalizado(false);
      } else {
        setFinalizado(true);
        cargarResultado(data);
      }
    } catch (err) {
      setError("Error al cargar la pregunta.");
    } finally {
      setLoading(false);
    }
  };

  const cargarResultado = (data) => {
    setResultado(data.resultado); // Guarda el resultado final
  };

  const enviarRespuesta = async (respuesta) => {
    await cargarPregunta(respuesta); // Pasa la respuesta del usuario
  };

  useEffect(() => {
    reiniciarConsulta();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-xl text-white animate-pulse">Cargando...</div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-xl text-red-500 font-semibold">{error}</div>
      </div>
    );
  }
  
  if (finalizado) {
    return (
      <div className="flex flex-col items-center justify-center h-full">
        <h2 className="text-3xl text-lime-300 font-extrabold mb-4 animate-bounce">
          ¡Respuestas completas!
        </h2>
        <pre className="mt-4 text-lg text-gray-800 bg-gray-100 p-4 rounded-lg shadow">{resultado}</pre>
        <button
          onClick={reiniciarConsulta}
          className="bg-pink-500 mt-4 text-white font-bold px-6 py-2 rounded-lg hover:bg-pink-600 transition duration-300 ease-in-out transform hover:scale-105"
        >
          Reiniciar Consulta
        </button>
      </div>
    );
  }

  return (
    <div className="bg-pink-50 p-6 rounded-lg shadow-lg w-96 max-h-[80vh] overflow-y-auto border border-pink-200">
      {pregunta && (
        <>
          <p className="text-lg text-center text-gray-800 mb-4 font-semibold">{pregunta}</p>
          <div className="flex justify-around mt-4">
            <button
              onClick={() => enviarRespuesta(true)}
              className="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition duration-300"
            >
              Sí
            </button>
            <button
              onClick={() => enviarRespuesta(false)}
              className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300"
            >
              No
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default GimnasiaData;


