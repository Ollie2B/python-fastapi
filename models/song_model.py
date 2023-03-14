from pydantic import BaseModel 

class Song(BaseModel):
    name: str
    artist: str