from fastapi import FastAPI
from settings.url import router
import uvicorn
from settings.db import DbInit
from repository.BaseModel import Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import asyncio
from models import User
app = FastAPI()
app.include_router(router)


db = DbInit()


@app.on_event("startup")
async def startup():
    await db.init_db()


uvicorn.run(app, host="0.0.0.0", port=8000)
