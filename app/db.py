from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL=""

engine=create_async_engine(DATABASE_URL,echo=True,future=True)
AsyncSessionLocal=sessionmaker(bind = engine, class_= AsyncSession, expire_on_commit=False)

Base=declarative_base()

async def get_session() -> AsyncSession: # type: ignore
    async with AsyncSessionLocal() as session:
        yield session

