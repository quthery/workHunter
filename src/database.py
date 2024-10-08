import asyncio
from typing import Annotated

from sqlalchemy import String, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from src.config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)

fabric_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(sync_engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
	type_annotation_map={
		str_256: String(256)
	}


