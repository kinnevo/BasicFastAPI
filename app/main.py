from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from .config import get_settings
from .routes import user

app = FastAPI(title="BasicFastAPI")
settings = get_settings()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.mongodb_url) # type: ignore
    app.mongodb = app.mongodb_client[settings.database_name]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close() # type: ignore

app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to BasicFastAPI"} 