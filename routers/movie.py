from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()



@movie_router.get('/movies', tags=['movies'])
def get_movies():
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(ge=1, le=1000)):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        raise JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(content=jsonable_encoder(result))





@movie_router.post('/movies', tags=['movies'])
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code= 201 ,content = {"message": "Movie created"})

@movie_router.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    db = Session()
    db_movie = MovieService(db).get_movie(id)
    if not db_movie:
        raise JSONResponse(status_code=404, content={"message": "Movie not found"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content=jsonable_encoder(db_movie), status_code=200)
        
        
@movie_router.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    db = Session()
    db_movie = MovieService(db).get_movie(id)
    if not db_movie:
        raise JSONResponse(status_code=404, content={"message": "Movie not found"})
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"message": "Movie deleted"}, status_code=200)  

