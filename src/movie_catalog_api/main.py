from typing import Annotated

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str = Field(min_length=2)
    year: int = Field(gt=1888)
    rating: float = Field(ge=0, le=10)


app = FastAPI()

movies = [
    {"id": 1, "title": "Inception"},
    {"id": 2, "title": "Interstellar"},
    {"id": 3, "title": "The Matrix"},
    {"id": 4, "title": "Gladiator"},
    {"id": 5, "title": "The Dark Knight"},
]

@app.get("/movies")
async def get_movies(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(gt=0, le=20)] = 10
):
    return movies[skip : skip + limit]

@app.get("/")
async def root():
    return {
        "message": "Welcome to Movie Catalog API"
    }

@app.get("/movies/top")
async def get_top_movie():
    return {
        "title": "The Dark Knight",
        "rating": 9.0
    }


@app.get("/movies/{movie_id}")
async def get_movie(
    movie_id: Annotated[int, Path(gt=0)]
):
    return {
        "movie_id": movie_id,
        "title": "Example Movie"
    }

@app.post("/movies")
async def create_movie(movie: Movie):
    return {
        "message": "Movie created successfully",
        "movie": movie
    }

@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, movie: Movie):
    return {
        "message": "Movie updated successfully",
        "movie_id": movie_id,
        "movie": movie
    }