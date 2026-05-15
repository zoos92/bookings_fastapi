from fastapi import APIRouter
from sqlalchemy import select
from dao.base import BaseDAO
from bookings.models import Bookings
from database import async_session_maker


class BookingDAO(BaseDAO):
    model = Bookings