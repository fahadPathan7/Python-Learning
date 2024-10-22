from fastapi import FastAPI, HTTPException
from schemas import GenreChoices, Band

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Beatles', 'members': 4, 'genre': 'genre1'},
    {'id': 2, 'name': 'The Rolling Stones', 'members': 5, 'genre': 'genre2'},
    {'id': 3, 'name': 'The Who', 'members': 4, 'genre': 'genre2'},
    {'id': 4, 'name': 'Led Zeppelin', 'members': 4, 'genre': 'genre4'},
    {'id': 5, 'name': 'Pink Floyd', 'members': 5, 'genre': 'genre4', 'album': [
        {'title': 'The Dark Side of the Moon', 'date': '1973-03-01'},
        {'title': 'The Wall', 'date': '1979-11-30'},
    ]},
    {'id': 6, 'name': 'Queen', 'members': 5, 'genre': 'genre3'},
]

@app.get('/')
async def index():
    return {'message': 'This is Home Page'}

@app.get('/bands')
async def bands() -> list[Band]:
    return [
        Band(**band) for band in BANDS # Band(**band) is equivalent to
            ## Band(id=band['id'], name=band['name'], members=band['members'], genre=band['genre'])
            ## returning all the attributes of the Band class
    ]

@app.get('/bands/{band_id}', status_code=206)
def bands_detail(band_id: int) -> Band:
    band = next((Band(**band) for band in BANDS if band['id'] == band_id), None)
    if band == None:
        raise HTTPException(status_code=404, detail='Band not found')
    else:
        return band

@app.get('/bands/{member_count}/members')
async def bands_with_same_members(member_count: int) -> list[dict]:
    return [
        band for band in BANDS if band['members'] == member_count
    ]

@app.get('/bands/{genre}/genre')
async def bands_with_same_genre(genre: str) -> list[dict]:
    return [
        band for band in BANDS if band['genre'] == genre
    ]