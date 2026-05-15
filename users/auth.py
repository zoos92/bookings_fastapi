from datetime import datetime, timedelta

from passlib.context import CryptContext
from pydantic import EmailStr
from users.dao import UsersDAO
from secrets import token_bytes
from base64 import b64encode


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, b64encode(token_bytes(32)).decode(), 'HS256')
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    existing_user = await UsersDAO.find_one_or_none(email=email)
    if not existing_user and not verify_password(password, existing_user.password):
        return None
    return existing_user