def song_serializer(song) -> dict:
    return {
        'id':str(song["_id"]),
        'name':song["name"],
        'artist':song["artist"]
    }

def songs_serializer(songs) -> list:
    return [song_serializer(song) for song in songs]