from sqlalchemy.orm import Session  # Import Session class from sqlalchemy.orm
from app.db import models  # Import models from app.db

# Función para publicar una película
def publicar_pelicula(pelicula, db: Session):
  """
  Publica una nueva película en la base de datos.
  """
  # Convierte el objeto de película a un diccionario
  pelicula = pelicula.model_dump()
  # Crea una nueva instancia del modelo Movie con los datos del diccionario
  nueva_pelicula = models.Movie(
      nombre_pelicula=pelicula["nombre_pelicula"],
      año_estreno=pelicula["año_estreno"],
      descripcion=pelicula["descripcion"],
      categoria=pelicula["categoria"],
  )
  # Agrega la nueva película a la sesión
  db.add(nueva_pelicula)
  # Guarda los cambios en la base de datos
  db.commit()
  # Refresca la instancia de la película para obtener sus datos actualizados
  db.refresh(nueva_pelicula)

# Función para obtener una película por su ID
def obtener_pelicula(pelicula_id, db: Session):
  """
  Obtiene una película específica por su ID.
  """
  # Busca la película en la base de datos por su ID
  pelicula = db.query(models.Movie).filter(models.Movie.id == pelicula_id).first()
  # Si no se encuentra la película, devuelve un mensaje de error
  if not pelicula:
    return {"respuesta": "película no encontrada"}
  # Al encontrarla Devuelve la película
  return pelicula

# Función para eliminar una película por su ID
def eliminar_pelicula(pelicula_id, db: Session):
  """
  Elimina una película de la base de datos por su ID.
  """
  # Busca la película en la base de datos por su ID
  pelicula = db.query(models.Movie).filter(models.Movie.id == pelicula_id)
  # Si no se encuentra la película, devuelve un mensaje de error
  if not pelicula.first():
    return {"respuesta": "película no encontrada"}
  # Al encontrarla Elimina la película de la sesión
  pelicula.delete(synchronize_session=False)
  # Guarda los cambios en la base de datos
  db.commit()
  # Devuelve un mensaje de confirmación
  return {"respuesta": "película eliminada correctamente"}

# Función para obtener todas las películas
def obtener_peliculas(db: Session):
  """
  Obtiene una lista de todas las películas de la base de datos.
  """
  # Consulta todas las películas en la base de datos
  data = db.query(models.Movie).all()
  # Devuelve la lista de películas
  return data

# Función para actualizar una película por su ID
def actualizar_pelicula(pelicula_id, updatePelicula, db: Session):
  """
  Actualiza una película existente en la base de datos.
  """
  # Busca la película en la base de datos por su ID
  pelicula = db.query(models.Movie).filter(models.Movie.id == pelicula_id)
  # Si no se encuentra la película, devuelve un mensaje de error
  if not pelicula.first():
    return {"respuesta": "película no encontrada"}
  # Actualiza la película con los datos del objeto updatePelicula
  pelicula.update(updatePelicula.model_dump(exclude_unset=True))
  # Guarda los cambios en la base de datos
  db.commit()
  # Devuelve un mensaje de confirmación
  return {"respuesta": "película actualizada correctamente"}
