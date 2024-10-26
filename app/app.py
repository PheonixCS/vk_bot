from fastapi import FastAPI
import uvicorn
from settings.db_init import DbInit
from repository.BaseModel import Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import asyncio
from settings.router import instance_router as base_router
from services.authorization.router import instance_router as auth_router


app = FastAPI()
app.include_router(base_router)
app.include_router(auth_router)

db = DbInit()


@app.on_event("startup")
async def startup():
    await db.init_db()


uvicorn.run(app, host="0.0.0.0", port=8000)
