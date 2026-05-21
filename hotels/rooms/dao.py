from sqlalchemy import select

from dao.base import BaseDAO
from hotels.rooms.models import Rooms
from database import async_session_maker


class RoomsDAO(BaseDAO):
    model = Rooms
