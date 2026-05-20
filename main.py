from fastapi import FastAPI, HTTPException, Request, Query
from pydantic import BaseModel, Field, EmailStr, ConfigDict
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
app = FastAPI()

# @app.get('/', summary='Main', tags=['hello'])
# def root():
#     return 'Hello world'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

# books = [
#     {
#         "id": 1,
#         "title": "Асинхронность в Python",
#         "author": "Мэттью"
#     },
#     {
#         "id": 2,
#         "title": "Backend разработка в Python",
#         "author": "Артём",
#     },
# ]

# @app.get(
#         '/books',
#         tags=['Books'],
#         summary='Get all books'
#         )
# def read_books():
#     return books


# @app.get(
#         '/book/{author}',
#          tags=['Books'],
#          summary='Get specific books'
#          )
# def get_book(author: Optional[str], book_id: Optional[int] = Query(None, gt=1)):
#     for book in books:
#         if book['id'] == book_id or book['author'] == author:
#             return book
#         else:
#             raise HTTPException(status_code=404, detail='Not found')

# class NewBook(BaseModel):
#     title: str
#     author: str

# @app.post(
#         '/books',
#          tags=['Books'],
#          summary='Create new book')
# def create_book(new_book: NewBook):
#     books.append({
#         'id': len(books) + 1,
#         'title': new_book.title,
#         'author': new_book.author
#     })
#     return {'success': True, 'message': 'Book is created'}


# if __name__ == '__main__':
#     uvicorn.run('main:app', host='0.0.0.0')


from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi import FastAPI, Depends, HTTPException, Response
from typing import Annotated, Callable, Optional
from sqlalchemy import select
import time
from bookings.routers import router as router_bookings
from users.router import router as router_users
from pages.router import router as pages_router

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(pages_router)

engine = create_async_engine('sqlite+aiosqlite:///books.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]


# @app.middleware('http')
# async def my_middleware(request: Request, call_next: Callable):
#     # ip = request.client.host
#     # print(f'{ip}')
#     # if ip in ['localhost', '127.0.0.1']:
#     #     return Response(status_code=429, content='Too many requests')
#     start = time.perf_counter()
#     response = await call_next(request)
#     end = time.perf_counter() - start
#     print(end)
#     response.headers['x-signature'] = 'Super'
#     return response

# class Base(DeclarativeBase):
#     pass

# class BookModel(Base):
#     __tablename__ = 'books'        

#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str]
#     author: Mapped[str]

# class BookGetSchema(BaseModel):
#     author: str
#     title: str

# class BookAddSchema(BaseModel):
#     author: str
#     title: str

# class BookSchema(BookAddSchema):
#     id: int

# class PaginationParams(BaseModel):
#     limit: int = Field(5, ge=0, lt=100, description='Кол-во эл-ов')
#     offset: int = Field(0, ge=0, description='Смещение')

# PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]

# @app.get('/books')
# async def get_books(
#     session: SessionDep,
#     pagination: PaginationDep,
# ) -> list[BookAddSchema]:
#     query = (
#         select(BookModel)
#         .limit(pagination.limit)
#         .offset(pagination.offset))
#     result = await session.execute(query)
#     return result.scalars().all()    

# @app.post('/setup_database')
# async def setup_database():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     return {'ok': True, 'msg': 'Base was set'}

# @app.post('/books')
# async def add_book(data: BookAddSchema, session: SessionDep):
#     new_book = BookModel(
#         title=data.title,
#         author=data.author,
#         )
#     session.add(new_book)
#     await session.commit()
#     return {'ok': True, 'msg': 'Book was add'}
    
# @app.get('/books')
# async def get_books(session: SessionDep):
#     query = select(BookModel)
#     result = await session.execute(query)
#     return result.scalars().all()

# from authx import AuthX, AuthXConfig

# config = AuthXConfig()
# config.JWT_SECRET_KEY = 'SECRET_KEY'
# config.JWT_ACCESS_COOKIE_NAME = 'my_access_token'
# config.JWT_TOKEN_LOCATION = ['cookies']

# security = AuthX(config=config)

# class UserLoginSchema(BaseModel):
#     username: str
#     password: str

# @app.post('/login')
# def login(creds: UserLoginSchema, respone: Response):
#     if creds.username == 'test' and creds.password == 'test':
#         token = security.create_access_token(uid='12345')
#         respone.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
#         return {'access_token': token}
#     raise HTTPException(status_code=401, detail='Incorrect')

# @app.get('/protected', dependencies=[Depends(security.access_token_required)])
# def protected():
#     return {'data': 'top_secret'}


# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import StreamingResponse, FileResponse

# app = FastAPI()

# @app.post('/files')
# async def upload_file(uploaded_file: UploadFile):
#     file = uploaded_file.file
#     filename = uploaded_file.filename
#     with open(f'1_{filename}', 'wb') as f:
#         f.write(file.read())
#     return filename

# @app.post('/mult_files')
# async def upload_files(uploaded_files: list[UploadFile]):
#     for uploaded_file in uploaded_files:
#         file = uploaded_file.file
#         filename = uploaded_file.filename
#         with open(f'1_{filename}', 'wb') as f:
#             f.write(file.read())
#     # return filename

# @app.get('/files/{filename}')
# async def get_file(filename: str):
#     return FileResponse(filename)

# def iterfile(filename: str):
#     with open('filename', 'rb') as file:
#         while chunk := file.read(1024*1024):
#             yield chunk


# @app.get('/files/streaming/{filename}')
# async def get_files(filename: str):
#     return StreamingResponse(iterfile(filename), media_type='video/mp4')

# class UserSchema(BaseModel):
#     email: EmailStr
#     bio: str | None = Field(max_length=10)

#     # model_config = ConfigDict(extra='forbid')

# class UserAgeSchema(UserSchema):    
#     age: int = Field(ge=0, le=120)
    
# user = UserSchema(**data)

# users = []

# @app.post('/users')
# def add_user(user: UserSchema):
#     users.append(user)
#     return {'ok': True, 'msg': 'User was add'}

# @app.get('/users')
# def get_users() -> list[UserSchema]:
#     return users

# def func(data_: dict):
#     data_['age'] += 1