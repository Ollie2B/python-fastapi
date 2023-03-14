from fastapi import APIRouter
from models.song_model import Song
from schemas.song_schema import songs_serializer
from bson import ObjectId
from config.db import collection

song = APIRouter()

@song.post("/songs", tags=["songs"])
async def create_song(song: Song):
    _id = collection.insert_one(dict(song))
    song = songs_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": song}

@song.get("/songs", tags=["songs"])
async def find_all_songs():
    songs = songs_serializer(collection.find())
    return {"status": "Ok","data": songs}

@song.get("/songs/{id}", tags=["songs"])
async def get_one_song(id: str):
    song = songs_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok","data": song}

@song.put("/songs/{id}", tags=["songs"])
async def update_song(id: str, song: Song):
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": dict(song)
        })
    song = songs_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok","data": song}

@song.delete("/songs/{id}", tags=["songs"])
async def delete_song(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "Ok","data": []} 