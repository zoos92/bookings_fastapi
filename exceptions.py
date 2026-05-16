from fastapi import Depends, HTTPException, Request, status

UserAlreasyExistException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail='User is already exist',
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Incorect pass/email'
    )

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Token expired',
)

TokenAbsentException =  HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Token absence',
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Incorrect format of token',
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
)