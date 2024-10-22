from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class MembersChoices(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

BANDS = [
    {'id': 1, 'name': 'The Beatles', 'members': 4},
    {'id': 2, 'name': 'The Rolling Stones', 'members': 5},
    {'id': 3, 'name': 'The Who', 'members': 4},
    {'id': 4, 'name': 'Led Zeppelin', 'members': 4},
    {'id': 5, 'name': 'Pink Floyd', 'members': 5},
    {'id': 6, 'name': 'Queen', 'members': 5},
]

@app.get('/')
async def index():
    return {'message': 'This is Home Page'}

@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get('/bands/{band_id}', status_code=206)
def bands_detail(band_id: int) -> dict:
    band = next((band for band in BANDS if band['id'] == band_id), None)
    if band == None:
        raise HTTPException(status_code=404, detail='Band not found')
    else:
        return band

@app.get('/bands/{member_count}/members')
async def bands_with_same_members(member_count: int) -> list[dict]:
    return [
        band for band in BANDS if band['members'] == member_count
    ]