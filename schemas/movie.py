from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=155)
    overview: str = Field(default='Descripcion de la película', min_length=8, max_length=500)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "title": "Movie Title",
                "overview": "Movie description",
                "year": 2022,
                "rating": 5.5,
                "category": "Action"
            }
        }