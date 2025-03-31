from fastapi import APIRouter, HTTPException

from .deps import *


router = APIRouter(tags=["Levels"])


@router.get("/get_levels")
def get_levels():
    levels = db.get_levels()
    if not levels:
        raise HTTPException(500, "Error occured while fetching levels!")
    return levels
