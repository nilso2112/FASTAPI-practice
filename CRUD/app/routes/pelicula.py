# Importamos clases necesarias de FastAPI
from fastapi import APIRouter, Depends

# Importamos las clases de esquema para películas (Movie, ShowMovie, UpdateMovie) desde app/schemas
from app.schemas import Movie, ShowMovie, UpdateMovie

# Importamos la función get_db para la sesión de la base de datos desde app/db/database
from app.db.database import get_db

# Importamos la clase Session de sqlalchemy.orm y el módulo typing
from sqlalchemy.orm import Session
from typing import List

# Importamos el objeto peli contiene funciones del repositorio de películas desde app/repository
from app.repository import peli

# Creamos un objeto APIRouter para los puntos finales de películas con prefijo "/pelicula" y etiqueta "peliculas"
router = APIRouter(
    prefix="/pelicula",
    tags=["peliculas"]
)


@router.get('/', response_model=List[ShowMovie])
def obtener_peliculas(db: Session = Depends(get_db)):
    """
    Obtiene una lista de todas las películas de la base de datos.
    """
    # Delega la obtención de películas a la función `obtener_peliculas` en `peli` función del repositorio
    data = peli.obtener_peliculas(db)
    # Devuelve la lista de películas en formato ShowMovie
    return data


@router.post('/')
def publicar_pelicula(pelicula: Movie, db: Session = Depends(get_db)):
    """
    Publica una nueva película en la base de datos.
    """
    # Delega la creación de la película a la función `publicar_pelicula` en `peli` función del repositorio
    peli.publicar_pelicula(pelicula, db)
    # Devuelve un mensaje de confirmación
    return {"respuesta": "Película publicada satisfactoriamente"}


@router.get('/{pelicula_id}', response_model=ShowMovie)
def obtener_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    """
    Obtiene una película específica por su ID.
    """
    # Delega la obtención de la película por ID a la función `obtener_pelicula` en `peli` función del repositorio)
    pelicula = peli.obtener_pelicula(pelicula_id, db)
    # Devuelve la película en formato ShowMovie
    return pelicula


@router.delete('/{pelicula_id}')
def eliminar_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    """
    Elimina una película de la base de datos por su ID.
    """
    # Delega la eliminación de la película por ID a la función `eliminar_pelicula` en `peli` función del repositorio)
    res = peli.eliminar_pelicula(pelicula_id, db)
    # Devuelve el resultado de la operación (posiblemente un mensaje de éxito o error)
    return res


@router.patch('/{pelicula_id}')
def actualizar_pelicula(pelicula_id: int, updatePelicula: UpdateMovie, db: Session = Depends(get_db)):
    """
    Actualiza una película existente en la base de datos.
    """
    # Delega la actualización de la película por ID a la función `actualizar_pelicula` en `peli` función del repositorio
    res = peli.actualizar_pelicula(pelicula_id, updatePelicula, db)
    # Devuelve el resultado de la operación (posiblemente un mensaje de éxito o error)
    return res
