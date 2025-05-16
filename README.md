Prueba FK - Aplicación de Registro de Eventos (Logs)

Este proyecto es una aplicación web desarrollada en Python con Flask, creada por Lina Estrada como parte de una prueba técnica. La aplicación permite registrar, consultar y filtrar eventos guardados en una base de datos MySQL.
Los eventos pueden ser ingresados manualmente mediante un formulario web o mediante una API.

Funcionalidades principales

- Registro de eventos a través de una **API REST** (`/api/register`)
- Registro manual de eventos mediante **formulario web** (`/form/register`)
- Consulta de eventos con filtros por **tipo de evento** y **rango de fechas**
- Registro de errores mediante archivos de **logging**
- Base de datos desacoplada usando **SQLAlchemy**

Tecnologías utilizadas
- Python 3.11+
- Flask
- SQLAlchemy
- PyMySQL
- MySQL Workbench
- HTML (con Jinja2 para los formularios)
- Logging para manejo de errores

Instalación y ejecución

1. Clonar el repositorio
git clone https://github.com/LINAESTRADA/Prueba-FK.git
cd Prueba-FK

2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

3.Instalar dependencias
pip install -r requirements.txt

4.Crear la base da datos MySQL
Desde MySQL Workbench, ejecuta:
CREATE DATABASE Registration;

5. Configurar la conexión a la base de datos
Edita el archivo config.py con tu contraseña de MySQL:

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:TU_CONTRASEÑA@localhost/Registration'
Reemplaza TU_CONTRASEÑA con tu contraseña real de MySQL.

6. Ejecutar la aplicación
python app.py

Endpoints disponibles
POST /api/register → Registra un evento vía API (requiere JSON con "description")

GET /form/register → Muestra el formulario de registro manual

GET /events → Consulta de eventos con filtros por fecha y tipo
