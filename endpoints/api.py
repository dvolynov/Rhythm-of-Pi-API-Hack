from fastapi import APIRouter

from .generation import router as generation_router
from .registration import router as registration_router
from .levels import router as levels_router


router = APIRouter()

router.include_router(generation_router, prefix='/generation')
router.include_router(registration_router, prefix='/registration')
router.include_router(levels_router, prefix='/levels')


