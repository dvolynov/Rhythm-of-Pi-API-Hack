from fastapi import APIRouter, Request, HTTPException

from .deps import *


router = APIRouter(tags=["User"])



# @error_handler(db)
@router.post("/add_user/{ip}/{hash}")
def add_user(ip: str, hash: str):
    response = db.add_user(ip, hash)
    if not response:
        raise HTTPException(500, "Error adding user in database!")
    return response