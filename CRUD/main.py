# Importa la clase FastAPI para construir APIs web en Python
from fastapi import FastAPI

# Importa el módulo uvicorn, un servidor ASGI popular para ejecutar aplicaciones FastAPI
import uvicorn

# Importa el ruteador `pelicula` del directorio `app.routes`
# (probablemente contiene funciones que definen puntos finales de la API para películas)
from app.routes import pelicula

# Importa la clase `Base` y el objeto `engine` del módulo `app.db.database`
# (`Base` es probablemente una clase base del modelo SQLAlchemy, y `engine` es una conexión a la base de datos)
from app.db.database import Base, engine

from core.config import Settings

# Función para crear tablas de la base de datos usando la clase `Base` (si no existen)
def create_tables():
  """
  Esta función crea todas las tablas definidas usando la clase `Base` en la base de datos.
  """
  Base.metadata.create_all(bind=engine)

# Llama a la función `create_tables`, probablemente para garantizar que las tablas se creen antes de iniciar la API
create_tables()

# Crea una instancia de la clase `FastAPI` para representar el núcleo de la API web
app = FastAPI()

# Incluye el ruteador `pelicula` en la aplicación principal
# Esto hace que los puntos finales de la API relacionados con películas sean accesibles a través de la ruta URL principal
app.include_router(pelicula.router)

# Establece el título y la versión de la API desde core.config.settings
app.title = Settings.PROJECT_NAME
app.version = Settings.PROJECT_VERSION

# Bloque condicional para asegurar que el siguiente código se ejecute solo cuando se ejecute el script directamente
if __name__ == "__main__":
  """
  Este bloque ejecuta la aplicación FastAPI usando el servidor uvicorn.
  """
  # Ejecuta la aplicación con estos argumentos:
  # - "main:app": Especifica el objeto de la aplicación a ejecutar (app del módulo actual)
  # - port=8000: Establece el puerto en el que la API escucha solicitudes (el predeterminado es 8000)
  # - reload=True: Habilita la recarga automática de la aplicación cuando se detectan cambios en el código
  uvicorn.run("main:app", port=8000, reload=True)
