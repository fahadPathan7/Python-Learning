
from enum import Enum
from pydantic import BaseModel
from datetime import date

class GenreChoices(Enum):
    genre1 = 'genre1'
    genre2 = 'genre2'
    genre3 = 'genre3'
    genre4 = 'genre4'

class Album(BaseModel):
    title: str
    date: date

class Band(BaseModel):
    # {'id': 1, 'name': 'The Beatles', 'members': 4, 'genre': 'genre1'},
    id: int
    name: str
    members: int
    genre: GenreChoices
    album: list[Album] = [] # list of Album objects (empty list by default)