from fastapi import FastAPI
from pymongo import MongoClient
import populartimes

client = MongoClient("localhost", 27017)

GOOGLE_MAPS_API_KEY = "AIzaSyCTV39OY2_5wmq6ZNB9CAeEvj6VdRZCYt8"
app = FastAPI()


@app.get("/populartimes/{placeId}")
async def get_popular_times(placeId: str):
    print(placeId)
    return populartimes.get_id(GOOGLE_MAPS_API_KEY, placeId)

@app.get("/sensors")
async def get_sensor_data():
    db = client.seoulro
    collection = db['sensor_data']
    return list(collection.find({}))[0]
