from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL_ASYNC = "postgresql+asyncpg://postgres:password@db:5432/flight_booking_db"

async_engine = create_async_engine(DATABASE_URL_ASYNC, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    bind=async_engine, expire_on_commit=False, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    """get database"""
    async with AsyncSessionLocal() as session:
        yield session
