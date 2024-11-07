from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Annotated, Any
from .config import get_settings
from .routes import user

class AppState(FastAPI):
    mongodb_client: AsyncIOMotorClient
    mongodb: AsyncIOMotorDatabase

@asynccontextmanager
async def lifespan(app: AppState):
    # Startup
    app.mongodb_client = AsyncIOMotorClient(settings.mongodb_url)
    app.mongodb = app.mongodb_client[settings.database_name]
    yield
    # Shutdown
    app.mongodb_client.close()

settings = get_settings()
app = AppState(title="BasicFastAPI", lifespan=lifespan)

app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to BasicFastAPI"} 