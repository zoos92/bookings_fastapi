from typing import Annotated, Any, Mapping

from annotated_doc import Doc
from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreasyExistException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail='User is already exist'

class IncorrectEmailOrPasswordException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Incorect pass/email'
    

class TokenExpiredException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Token expired'


class TokenAbsentException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Token absence'


class IncorrectTokenFormatException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Incorrect format of token'

class UserIsNotPresentException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED