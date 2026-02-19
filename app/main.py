from sqlmodel import SQLModel
from core.database import engine
from fastapi import FastAPI
from routes.conversation_routes import router as conversation_router
from routes.game_routes import router as game_router
from fastapi.middleware.cors import CORSMiddleware

SQLModel.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dooman-git-main-bilalshahid707s-projects.vercel.app"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(conversation_router)
app.include_router(game_router)
