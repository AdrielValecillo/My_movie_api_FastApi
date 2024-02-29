from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService:
    def __init__(self, db):
        self.db = db
        
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return new_movie
    
    def update_movie(self, id: int, movie: Movie):
        db_movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not db_movie:
            return None
        db_movie.title = movie.title
        db_movie.overview = movie.overview
        db_movie.year = movie.year
        db_movie.rating = movie.rating
        db_movie.category = movie.category
        self.db.commit()
        return db_movie
    
    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return
        