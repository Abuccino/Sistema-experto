# sistema-experto-python
Sistema Experto para la Enseñanza de Saltos en Gimnasia Artística

----------
Carrera: Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial
Institución: Politécnico Malvinas Argentinas Web
Materia: Desarrollo de Sistemas de IA
Año: 2024
desarrolladora: Buccino Anabella

----------
# Descripción del Proyecto:
El sistema experto ha sido diseñado para capacitar a profesores de gimnasia artística y profesores de educación física en la enseñanza de los saltos al Vault (cajón de salto, mesa o bóveda). Este sistema aborda diversas ejecuciones técnicas y niveles de dificultad que son requeridos por el código de gimnasia artística. Los saltos se enseñan en función del desarrollo de habilidades motoras y niveles de competencia de los alumnos, permitiendo un enfoque progresivo en el aprendizaje
Objetivo
El objetivo del sistema es proporcionar un enfoque estructurado para enseñar saltos en gimnasia artística, considerando:

-Tipo de entrada al cajón de salto.
-Nivel de dificultad de los saltos.
-Coordinación necesaria para la ejecución correcta.
-Salida del cajón, que puede incluir giros o mortales.


# Descripción
Este proyecto es un sistema experto desarrollado para ayudar en la toma de decisiones relacionadas con saltos de gimnasia artística. Utilizando un backend basado en FastAPI y un frontend construido con React, el sistema permite hacer consultas y obtener recomendaciones sobre diferentes saltos de gimnasia basados en respuestas sí/no.

# Funcionalidad
Frontend: Se utiliza React para mostrar las preguntas del sistema experto y permitir a los usuarios responderlas.
Backend: FastAPI gestiona las consultas y el motor de inferencia, proporcionando las preguntas y respuestas en tiempo real.
Base de Conocimiento: El sistema carga un archivo JSON que contiene la base de conocimiento sobre los saltos de gimnasia. La base de conocimiento es consultada y utilizada para generar las preguntas.

---------
Estructura del Proyecto

/
├── backend/                        # Backend en FastAPI
│   ├── main.py                     # Archivo principal de la API
│   ├── acciones.py                 # Lógica para manejar las respuestas y consultar la base de conocimiento
│   ├── base_conocimiento.json      # Base de conocimiento en formato JSON
├── frontend/                       # Frontend con React
│   ├── GimnasiaData.js             # Componente React principal
│   ├── package.json                # Dependencias y scripts de React
│   └── public/                     # Archivos estáticos de React
├── README.md                       # Documentación del proyecto
└── .gitignore                      # Archivos que deben ser ignorados por Git
-----------

## Instalación
# Backend (FastAPI)

**1-**Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd sistemaIA-master
```
**2-**Instalar dependencias

Asegúrate de tener pipenv instalado. Si no lo tienes, instálalo usando:

```bash
pip install pipenv
```
Luego, instala las dependencias del backend:

```bash
pipenv install
```

**3-**Ejecutar el servidor

Activa el entorno virtual:

```bash
pipenv shell
```
Inicia el servidor FastAPI:

```bash
uvicorn main:app --reload
```
si no se logra ejecutar con el código de arriba el main probar con el siguiente código en la terminal

```bash
python3 -m uvicorn main:app --reload 
```
El servidor estará corriendo en http://127.0.0.1:8000.
------------
# Frontend (React)

**1-**Instalar dependencias de React

Navega al directorio frontend y ejecuta:

```bash
npm install
```

**2-**Ejecutar el frontend
Dentro del directorio sistema-experto-gimnasia

Para ejecutar la aplicación en modo de desarrollo:

```bash
npm run dev
```
El frontend estará disponible en http://localhost:3000.
------------
# Funcionamiento

# Backend
[-] **Cargar la base de conocimiento:** El backend expone una ruta POST /base/cargar para cargar la base de conocimiento (el archivo gimnasia.json).
[-] **Iniciar la consulta:** La ruta GET /consultar/iniciar devuelve la primera pregunta para iniciar el proceso de consulta.
[-] **Responder las preguntas:** La ruta POST /consultar/responder recibe las respuestas sí/no del usuario y avanza en la consulta. Cuando el proceso se completa, devuelve un resultado final.

# Frontend
El componente GimnasiaData.js gestiona la interacción con el usuario. Los pasos son los siguientes:

[-] **Cargar la base de conocimiento:** El frontend inicia la consulta llamando a POST /base/cargar para cargar los datos desde el archivo gimnasia.json.
[-] **Hacer preguntas:** Se obtiene una pregunta inicial desde la ruta GET /consultar/iniciar y se muestra al usuario.
[-] **Responder:** El usuario responde "Sí" o "No", y el frontend envía esta respuesta a través de POST /consultar/responder.
[-] **Resultado final:** Cuando todas las preguntas han sido respondidas, el sistema muestra un resultado final.

# Componentes Principales:

**GimnasiaData.js:** Este componente React es el núcleo de la interfaz de usuario. Gestiona el estado de la consulta, carga las preguntas y muestra los resultados.
**reiniciarConsulta:** Resetea el estado y vuelve a cargar el archivo JSON.
**cargarJson:** Llama a la API para cargar el archivo JSON de la base de conocimiento.
**iniciarConsulta:** Hace una llamada a la API para obtener la primera pregunta.
**cargarPregunta:** Envía la respuesta del usuario a la API y obtiene la siguiente pregunta o el resultado final.
**cargarResultado:** Muestra el resultado final de la consulta.
------------

# Dependencias
# Backend

FastAPI: Framework web moderno y rápido para crear APIs con Python.
uvicorn: Servidor ASGI para correr FastAPI.
pydantic: Validación de datos para los modelos de FastAPI.

# Frontend
React: Biblioteca de JavaScript para crear interfaces de usuario.
axios: Cliente HTTP para hacer solicitudes desde React.
-----------
# Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

