from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy import select
from bookings.dao import BookingDAO
from bookings.models import Bookings
from bookings.schemas import SBooking
from database import async_session_maker
from users.dependencies import get_current_user
from users.models import Users
from exceptions import RoomCannotBeBooked


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)

@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    result = BookingDAO.find_all(user_id=user.id)
    return await result

# @router.post('')
# async def add_booking(user: Users = Depends(get_current_user)):
#     await BookingDAO.add(user_id=user.id)    

@router.get('/get_book_by_id')
async def get_book_by_id():
    result = BookingDAO.find_by_id(4)
    return await result

@router.get('/get_one_or_none')
async def get_book_one_or_none():
    result = BookingDAO.find_one_or_none(room_id=1)
    return await result

@router.post('/add_booking')
async def add_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user)
):
    
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
    