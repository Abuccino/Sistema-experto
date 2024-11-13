# python3 -m uvicorn main:app --reload   -> este comando ejecuta el backend de main.py desde el directorio : sistemasIA-master

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from acciones import engine
from experto_general.response import Response

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Este es el puerto de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)


# Modelos de Pydantic para los datos
class FilenameRequest(BaseModel):
    filename: str

class UserResponse(BaseModel):
    response: bool  # True para "Sí", False para "No"

# Función auxiliar para cargar el JSON y agregar la clave "preguntas"
def cargar_preguntas():
    try:
        with open("gimnasia.json", "r", encoding="utf-8") as file:
            # Cargar el contenido original del archivo
            data = json.load(file)
            
            # Envolver la lista de preguntas dentro de la clave 'preguntas'
            return {"preguntas": data}  # Aquí envolvemos los datos bajo la clave 'preguntas'
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo JSON: {str(e)}")

# Endpoint para cargar la base de conocimientos desde un archivo JSON
@app.post("/base/cargar")
async def cargar_base(request: FilenameRequest):
    try:
        # Simulación de carga del archivo JSON
        engine.base.from_json(request.filename)
        return {"message": "Base de conocimientos cargada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para iniciar una consulta con el sistema experto
@app.get("/consultar/iniciar")
async def iniciar_consulta():
    # Inicia el generador de preguntas
    engine.questions = engine.generate()
    return siguiente_pregunta()

# Endpoint para procesar la respuesta del usuario y obtener la siguiente pregunta
@app.post("/consultar/responder")
async def responder_pregunta(request: UserResponse):
    if not hasattr(engine, 'questions'):
        raise HTTPException(status_code=400, detail="La consulta no ha sido iniciada. Llame primero a /consultar/iniciar.")

    # Configura la respuesta del usuario en el motor
    engine.set_response(Response.YES if request.response else Response.NO)
    return siguiente_pregunta()

# Función auxiliar para obtener la siguiente pregunta o el resultado final
def siguiente_pregunta():
    try:
        pregunta = next(engine.questions)  # Obtener la siguiente pregunta
        if pregunta:  # Si hay una pregunta disponible
            return {"pregunta": f"¿{pregunta.name}?"}
        else:  # Si no hay más preguntas, devolver el resultado
            resultado = engine.get_result()
            if resultado:
                return {
                    "resultado": f"Diagnostico: {resultado.name}",
                    "descripcion": resultado.description,
                    "propiedades": [prop.name for prop in resultado.properties]
                }
            else:
                return {"resultado": "No se encontró ninguna coincidencia"}
    except StopIteration:
        return {"resultado": "No se encontró ninguna coincidencia"}
