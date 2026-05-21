from datetime import date

from sqlalchemy import and_, func, or_, select

from bookings.models import Bookings
from dao.base import BaseDAO
from hotels.models import Hotels
from database import async_session_maker
from hotels.rooms.models import Rooms


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def searching_str(cls, column_name: str, string: str):
        async with async_session_maker() as session:
            column = getattr(cls.model, column_name)
            query = select(cls.model).filter(column.like(f'%{string}%'))
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def rooms_left(
        cls,
        hotel: Hotels,        
        #room_id: int,
        date_from: date,
        date_to: date):
        
        for room_id in Rooms.id:
            async with async_session_maker() as session:
                    booked_rooms = select(Bookings).where(and_
                                                        (or_(
                                                        and_(
                                                            Bookings.date_from >= date_from, Bookings.date_from <= date_to),
                                                        and_(
                                                            Bookings.date_to >= date_from, Bookings.date_to <= date_to
                                                            ))),
                                                            Bookings.room_id == room_id).cte('booked_rooms')
                    get_rooms_left = select(
                        (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
                        ).select_from(Rooms).join(
                            booked_rooms, booked_rooms.c.room_id == Rooms.id
                        ).where(Rooms.id == room_id).group_by(
                            Rooms.quantity, booked_rooms.c.room_id
                        )
                    #print(get_rooms_left.compile(engine, compile_kwargs={'literal_binds': True}))

                    rooms_left = await session.execute(get_rooms_left)
                    rooms_left = rooms_left.scalar()