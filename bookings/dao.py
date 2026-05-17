from datetime import date

from fastapi import APIRouter
from sqlalchemy import and_, or_, select
from dao.base import BaseDAO
from bookings.models import Bookings
from database import async_session_maker


class BookingDAO(BaseDAO):
    model = Bookings

    # @classmethod
    # async def add(
    #     cls,
    #     date_from: date,
    #     date_to: date,
    #     ):
    #     booked_rooms = select(Bookings).where(and_(
    #         Bookings.room_id == 1,
    #         or_(
                
    #         )
    #     ))        
