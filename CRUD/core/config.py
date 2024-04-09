import os  # Importa el módulo 'os' para interactuar con el sistema operativo

# Importa la función 'load_dotenv' de la librería 'dotenv' para cargar variables de entorno
from dotenv import load_dotenv

# Importa la clase 'Path' del módulo 'pathlib' para trabajar con rutas de archivos
from pathlib import Path

# Define la ruta al archivo '.env' relativa al directorio de trabajo actual
env_path = Path('.') / '.env'

# Carga las variables de entorno desde el archivo '.env' especificado
load_dotenv(dotenv_path=env_path)

# Define una clase llamada 'Settings' para almacenar la configuración de la aplicación
class Settings:
  """
  Esta clase almacena configuraciones para la aplicación.
  """
  # Define el nombre de la aplicación como una constante de cadena
  PROJECT_NAME: str = "MI PRIMERA API"

  # Define la versión del proyecto como una constante de cadena
  PROJECT_VERSION: str = "1.0"

  # Recupera el nombre de la base de datos de la variable de entorno 'POSTGRES_DB'
  POSTGRES_DB: str = os.getenv('POSTGRES_DB')

  # Recupera el usuario de la base de datos de la variable de entorno 'POSTGRES_USER'
  POSTGRES_USER: str = os.getenv('POSTGRES_USER')

  # Recupera la contraseña de la base de datos de la variable de entorno 'POSTGRES_PASSWORD' 
  POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')

  # Recupera el nombre de host o IP del servidor de la base de datos de la variable de entorno 'POSTGRES_SERVER'
  POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')

  # Recupera el puerto de la base de datos de la variable de entorno 'POSTGRES_PORT'
  POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')

  # Construye la URL de conexión a la base de datos usando variables de entorno recuperadas
  DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Crea una instancia de la clase Settings para acceder a la configuración de la aplicación
settings = Settings()
