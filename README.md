Proyecto Final Integrador: Sistema Ciberfísico y Gemelo Digital

Middleware IoT desarrollado en Python (FastAPI) que conecta un prototipo físico (ESP32) con un Gemelo Digital en Unity, utilizando MQTT para la transmisión de datos en tiempo real y MongoDB para el almacenamiento histórico.

Instrucciones de Instalación y Ejecución

Sigue estos pasos para levantar el entorno de desarrollo local.

1. Configuración del Entorno Python

Si es la primera vez que descargas el proyecto, crea el entorno virtual:

python -m venv .venv

Activa el entorno virtual (Windows):

.venv\Scripts\activate

2. Infraestructura (Docker)

Levanta los servicios de base de datos (MongoDB) y el broker de mensajería (Mosquitto):

docker-compose up -d

3. Instalación de Dependencias

Una vez activado el entorno virtual, instala las librerías requeridas:

pip install -r requirements.txt

4. Ejecución del Middleware

Navega a la carpeta de código fuente e inicia el servidor:

cd src
uvicorn main:app --reload

🔗 Enlaces Útiles

API Server: http://127.0.0.1:8000

Documentación Interactiva (Swagger): http://127.0.0.1:8000/docs

MongoDB (Local): mongodb://localhost:27017

Broker MQTT: tcp://localhost:1883
