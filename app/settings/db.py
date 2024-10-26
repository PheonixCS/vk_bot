from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from repository.BaseModel import Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import os
from sqlalchemy_utils import database_exists, create_database
from models import *
class DbInit:
    def __init__(self):
        self.DATABASE_URL = os.environ['DATABASE_URL']
        self.engine = create_async_engine(self.DATABASE_URL, echo=True)
    async def _create_engine(self):
        
        engine = create_async_engine(
            self.DATABASE_URL,
            echo=True,
        )
        return engine

    async def _create_session(self):
        SessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        return SessionLocal
    
    async def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    async def init_db(self):
        # Предположим, что у вас есть URL базы данных
        DATABASE_URL = self.DATABASE_URL
        # Создаем асинхронные сессии
        async with self.engine.begin() as conn:
            # Создать все таблицы
            await conn.run_sync(Base.metadata.create_all)
        await self.engine.dispose()