from fastapi import APIRouter
from sqlalchemy import select
from bookings.dao import BookingDAO
from bookings.models import Bookings
from bookings.schemas import SBooking
from database import async_session_maker


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)

@router.get('')
async def get_bookings() -> list[SBooking]:
    result = BookingDAO.find_all()
    return await result

@router.get('/get_book_by_id')
async def get_book_by_id():
    result = BookingDAO.find_by_id(4)
    return await result

@router.get('/get_one_or_none')
async def get_book_one_or_none():
    result = BookingDAO.find_one_or_none(room_id=1)
    return await result