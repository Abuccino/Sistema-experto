// App.jsx
import React from "react";
import GimnasiaData from "./components/GimnasiaData";
import './index.css';

function App() {
  return (
    <div className="bg-red-500 w-full h-screen flex flex-col justify-around items-center p-4">
      <h1 className="text-5xl text-red-300 text-center">Anabella Buccino</h1>
      <h1 className="text-white text-4xl text-center font-bold -mt-40">Sistema Experto de Gimnasia</h1>
      <div className="w-full flex justify-center -mt-40">
        <GimnasiaData />
      </div>
    </div>
  );
}

export default App;



