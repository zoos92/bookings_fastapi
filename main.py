from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import FastAPI, Depends
from typing import Annotated

from bookings.routers import router as router_bookings
from users.router import router as router_users
from pages.router import router as pages_router
from hotels.routers import router as hotels_router


app = FastAPI()

app.include_router(hotels_router)
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(pages_router)

engine = create_async_engine('sqlite+aiosqlite:///books.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]