from fastapi import APIRouter, Request, HTTPException
import json

from modules import SunoAPI
from .deps import *


router = APIRouter(tags=["Generation"])

suno_client = SunoAPI(auth_token=SUNO_TOKEN, save_directory=SAVE_DIRECTORY)


@router.post("/generate_audio/{prompt}/{hash}")
async def audio(prompt: str, hash: str):
    task = await suno_client.create_task(
        prompt        = prompt,
        custom_mode   = CUSTOM_MODE,
        instrumental  = INSTRUMENTAL,
        model         = MODEL,
        callback_url  = f"{DOMAIN}/api/generation/callback/{hash}"
    )
    return task["data"]["taskId"]


@router.post("/callback/{hash}")
async def callback(request: Request, hash: str):
    data = await request.json()

    if data.get("code") != 200 or data["data"]["callbackType"] != "complete":
        raise HTTPException(400, "Incomplete or failed generation!")

    task_id = data["data"]["task_id"]
    audio = data["data"]["data"][0]

    new_song = db.add_song(
        title     = audio["title"],
        duration  = audio["duration"],
        tags      = audio["tags"],
        url       = audio["audio_url"],
        task_id   = task_id,
        image_url = audio["image_url"],
        hash      = hash
    )
    if not new_song:
        raise HTTPException(500, "Error adding song in database!")
    return new_song


@router.get("/get_audio/{hash}/{task_id}")
def get_audio(hash: str, task_id: str):
    user = db.get_user(hash)
    if not user:
        raise HTTPException(500, "User not found!")
    song = db.get_song(user.id, task_id)
    if not song:
        raise HTTPException(404, "Error occured while fetching the audio!")


    return song
