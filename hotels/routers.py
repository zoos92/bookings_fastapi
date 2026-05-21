from datetime import date

from fastapi import APIRouter, Response

from database import Base
from hotels.dao import HotelsDAO
from hotels.models import Hotels
from hotels.schemas import SearchHotels


router = APIRouter(
    prefix='/hotels',
    tags=['Hotels']
    )

# @router.get('')
# async def get_hotels(location: str):
#     result = HotelsDAO.find_all(location = location)
#     return await result

@router.get('/{location}')
async def get_hotels_by_loc(location: str):
    # location = 
    result = HotelsDAO.searching_str(column_name='location', string=location)
    return await result

