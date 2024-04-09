#from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Modelo Pydantic para una película (se usa para la creación)
class Movie(BaseModel):
  """
  Modelo de datos para una película. Se utiliza para Publicacioon de nuevas películas.
  """
  nombre_pelicula: str  # Nombre de la película (obligatorio)
  año_estreno: int  # Año de estreno (obligatorio)
  descripcion: str  # Descripción de la película (opcional)
  categoria: str  # Categoría de la película (obligatoria)
  fecha_publicacion: datetime = datetime.now()  # Fecha de publicación (por defecto, la fecha actual)

# Modelo Pydantic para actualizar una película (se usa para la modificación)
class UpdateMovie(BaseModel):
  """
  Modelo de datos para actualizar una película. Los campos no especificados se mantienen sin cambios.
  """
  nombre_pelicula: str = None  # Nombre de la película (opcional)
  año_estreno: int = None  # Año de estreno (opcional)
  categoria: str = None # Categoría de la película (opcional)
  descripcion: str = None  # Descripción de la película (opcional)

# Modelo Pydantic para mostrar una película (se usa para la visualización)
class ShowMovie(BaseModel):
  """
  Modelo de datos para mostrar información de una película.
  """
  id: int  # ID de la película
  nombre_pelicula: str  # Nombre de la película
  año_estreno: int  # Año de estreno
  descripcion: str  # Descripción de la película
  categoria: str  # Categoría de la película

  class Config():
    """
    Configuración para el modelo ShowMovie.
    """
    fom_attributes = True  # Indica que el modelo se usará con un antes llamado ORM (Object-Relational Mapping)

