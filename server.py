from fastapi import FastAPI

app = FastAPI()

@app.get("/ping", tags=["example"])
async def test():
    return {"message": "Pong"}

from routes.song_routes import song
app.include_router(song)