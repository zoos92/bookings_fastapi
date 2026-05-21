from pydantic import BaseModel
# from bookings.dao import roo


class SearchHotels(BaseModel):
    location: str