from fastapi import FastAPI
import populartimes

GOOGLE_MAPS_API_KEY = "AIzaSyCTV39OY2_5wmq6ZNB9CAeEvj6VdRZCYt8"
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/populartimes/{placeId}")
async def get_popular_times(placeId: str):
    print(placeId)
    return populartimes.get_id(GOOGLE_MAPS_API_KEY, placeId)
