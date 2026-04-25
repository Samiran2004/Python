
from typing import Optional

from fastapi import APIRouter, Depends, File, Form, UploadFile

from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import UserResponse

from ..service.user_service import delete_user_service, get_current_user_service, register_user_service, update_user_service, user_login_service

from ..db import User, get_async_session


router = APIRouter(
    prefix='/api/v1/users',
    tags=['User']
)

@router.post('/register')
async def user_registration(
    fullname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    profile_image: Optional[UploadFile] = File(None),
    db: AsyncSession = Depends(get_async_session)
):
    return await register_user_service(
        fullname=fullname,
        email=email,
        password=password,
        profile_image=profile_image,
        db=db
    ) #type:ignore

@router.post('/login')
async def user_login(
    email: str,
    password: str,
    db: AsyncSession = Depends(get_async_session)
):
    return await user_login_service(
        email=email,
        password=password,
        db=db
    )

@router.get('/me', response_model=UserResponse)
async def get_logged_in_user(current_user: User = Depends(get_current_user_service)):
    return current_user 

@router.patch('/me', response_model=UserResponse)
async def update_loggedin_user(
    fullname: Optional[str] = Form(None),
    profile_image: Optional[UploadFile] = File(None),
    current_user: User = Depends(get_current_user_service),
    db: AsyncSession = Depends(get_async_session)
):
    return await update_user_service(
        current_user=current_user,
        fullname=fullname,
        profile_image=profile_image,
        db=db
    )

@router.delete('/me')
async def delete_loggedin_user(
    current_user: User = Depends(get_current_user_service),
    db: AsyncSession = Depends(get_async_session)
):
    return await delete_user_service(current_user=current_user, db=db)