from fastapi import FastAPI
from app.routers import books
from app.db import engine, Base

app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as connection:
#         await connection.run_sync(Base.metadata.create_all)

# @app.on_event("shutdown")
# async def shutdown():
#     await engine.dispose()

app.include_router(books.router)