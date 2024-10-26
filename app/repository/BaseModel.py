from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import os
from settings.db_init_worker import async_session_maker 
class Base(AsyncAttrs, DeclarativeBase): 
    __abstract__ = True
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            
            query = select(cls).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    @classmethod
    async def add(cls, **kwargs):
        async with async_session_maker() as session:
            object = cls(**kwargs)
            session.add(object)
            await session.commit()