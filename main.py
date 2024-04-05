from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str
    
class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str
    
class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)
    
    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 1,
                'title': 'My movie',
                'overview': 'Esta Pelicula trata acerca de ...',
                'year': 2024,
                'rating': 5,
                'category': 'comedia'
            }
        }
    }

movies: List[Movie] = []

app.title = "Mi primera Chamba"
app.version = "1.0"

@app.get('/', tags=['Home'])
def home():
    return "Hol python!"

@app.get('/movies', tags=['Movies'])
def get_movies() -> List[Movie]:
    return [movie.model_dump() for movie in movies]

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return movie.model_dump()
    return{}

@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:
    for movie in movies:
        if movie.category == category:
            return movie.model_dump()
    return {}


@app.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie)    
    return [movie.model_dump() for movie in movies]

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
    return [movie.model_dump() for movie in movies]
            
@app.delete('/movies/{id}', tags=['Movies'])  
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return [movie.model_dump() for movie in movies]
              
            