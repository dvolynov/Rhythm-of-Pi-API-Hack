from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints import router


app = FastAPI(title="RHYTHM OF PI")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix='/api')