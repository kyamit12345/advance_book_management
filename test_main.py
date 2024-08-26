import pytest
from httpx import AsyncClient,ASGITransport
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app
from app.db import get_session, engine, Base

@pytest_asyncio.fixture(scope="module")
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app),base_url="http://test") as client:
        yield client

@pytest_asyncio.fixture(scope="module")
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metdata.create_all)
    async with AsyncSession(engine) as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_insert_book(async_client):
    response= await async_client.post("/books/",json={"title":"Book1","author":"ABC","genre":"XYZ","year_published":"2010","summary":"ABC"})
    assert response.status_code ==200
    data=response.json()
    assert data["title"] == "Book1"