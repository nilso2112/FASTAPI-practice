# Importamos librerías necesarias de SQLAlchemy
from sqlalchemy import create_engine  # Crea una conexión de motor de base de datos
from sqlalchemy.ext.declarative import declarative_base  # Clase base para crear modelos de base de datos
from sqlalchemy.orm import sessionmaker  # Crea objetos de sesión de base de datos

# Importamos la URL de la base de datos desde core.config.settings
from core.config import settings
SQLAlCHEMY_DATABASE_URL = settings.DATABASE_URL  # Asigna la URL de la base de datos desde settings

# Crea una conexión de motor de base de datos usando la URL proporcionada
engine = create_engine(SQLAlCHEMY_DATABASE_URL)

# Crea una clase sessionmaker vinculada al motor con configuraciones específicas
SessionLocal = sessionmaker(
    autocommit=False,  # Deshabilita la confirmación automática de transacciones en cada operación
    autoflush=False,   # Deshabilita el vaciado automático de cambios a la base de datos
    bind=engine       # Vincula sessionmaker al motor creado
)

# Define una clase base declarativa para crear modelos de base de datos
Base = declarative_base()  # Heredar de esta clase crea modelos de base de datos

# Función para obtener una sesión de la base de datos
def get_db():
  """
  Esta función crea un nuevo objeto de sesión de la base de datos y lo cede para su uso.
  Asegura el cierre adecuado de la sesión después de su uso.
  """
  db = SessionLocal()
  try:
    yield db  # Cede el objeto de sesión para interacciones con la base de datos
  finally:
    db.close()  # Cierra el objeto de sesión para liberar recursos
