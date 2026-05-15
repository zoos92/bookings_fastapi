from fastapi import APIRouter, HTTPException, status

from users.auth import authenticate_user, get_password_hash, verify_password
from users.dao import UsersDAO
from users.models import Users
from users.schemas import SUserAuth

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password[:72])
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)

@router.post('/login')
async def login_user(user_data: SUserAuth):
    existing_user = await authenticate_user(user_data.email, user_data.password)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = cre
