from fastapi import FastAPI
from config.database import engine, Base
from middleware.error_handler import Error_handler
from routers.movie import movie_router

app = FastAPI()
app.title = "Movie API"
app.add_middleware(Error_handler)

app.include_router(movie_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

