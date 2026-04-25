from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends 
from typing import Optional

from .router.uploader import router as upload_router
from .router.userRouter import router as user_router

from .schemas import PostCreate, PostResponse

from .db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(
    title="Media Sharing Application",
    description="<https://youtu.be/SR5NYCdzKkc?si=0_-YSyS1iNRGVsLC>",
    lifespan=lifespan
)

app.include_router(upload_router)
app.include_router(user_router)

@app.get('/hello_world')
def hello_world():
    return {
        'message': "Hello World!"
    }