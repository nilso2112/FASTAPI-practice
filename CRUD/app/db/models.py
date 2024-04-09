#from sqlalchemy.schema import ForeignKey
#from sqlalchemy.orm import relationship


# Importa la clase Base del módulo app.db.database (probablemente una clase base del modelo SQLAlchemy)
from app.db.database import Base

# Importa los tipos de datos necesarios de SQLAlchemy para definir columnas de la base de datos
from sqlalchemy import Column, Integer, String, Boolean, DateTime

# Importa la clase datetime para manejar fechas y horas
from datetime import datetime

# Define una clase llamada Movie que hereda de la clase Base
class Movie(Base):
  """
  Esta clase define un modelo para una entidad de película en la base de datos.
  """

  # Define el nombre de la tabla en la base de datos
  __tablename__ = "peliculas"  # "peliculas" 

  # Define la columna de ID de película con tipo de dato, clave primaria y autoincremento
  id = Column(Integer, primary_key=True, autoincrement=True)

  # Define la columna de nombre de película con tipo de dato string y restricción única (sin nombres duplicados)
  nombre_pelicula = Column(String, unique=True)

  # Define la columna de año de estreno con tipo de dato entero
  año_estreno = Column(Integer)  # "año de estreno" 

  # Define la columna de descripción de la película con tipo de dato string
  descripcion = Column(String)  # "descripcion" 

  # Define la columna de fecha de publicación con tipo de dato, valor predeterminado (fecha y hora actual) y actualización automática al cambiar
  fecha_publicacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)  # "fecha de publicación" 

  # Define la columna de disponibilidad de la película con tipo de dato y valor predeterminado (False)
  estado = Column(Boolean, default=False)  # "estado" 

  # Define la columna de categoría de la película con tipo de dato string
  categoria = Column(String)  # "categoria"
    #categoria = relationship("categoria",backref="pelicula",cascade="delete,merge")
    
"""class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre_pelicula_id = Column(Integer,ForeignKey("pelicula.id",ondelete="CASCADE"))
    categoria = Column(String)"""