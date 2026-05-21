from fastapi import APIRouter
from hotels.rooms.dao import RoomsDAO
from hotels.routers import router

@router.get('/rooms')
async def get_rooms():
    result = RoomsDAO.find_all()
    return await result

