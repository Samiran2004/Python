from fastapi import Depends, HTTPException, Header, UploadFile, status
import jwt
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..libs.security import ALGORITHM, SECRET_KEY, create_access_token, get_password_hash, verify_password

from ..libs.cloudinary import delete_image, upload_image

from ..db import Post, User, get_async_session


async def register_user_service(
    fullname: str,
    email: str,
    password: str,
    profile_image: UploadFile | None,
    db: AsyncSession
):
    # Check if the user is already exists
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered"
        )
    
    # Upload profile image to cloudinary if provided...
    profile_image_url = None
    if profile_image:
        cloudinary_response = await upload_image(profile_image)
        profile_image_url = cloudinary_response.get("secure_url")
    
    hashed_pwd = get_password_hash(password=password)
    
    new_user = User(
        fullname = fullname,
        email = email,
        hashed_password = hashed_pwd,
        profile_image_url = profile_image_url
    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user


async def user_login_service(
    email: str,
    password: str,
    db: AsyncSession
):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(password, user.hashed_password): #type:ignore
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Email or Password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )
    
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    


async def get_current_user_service(
    x_token: str = Header(..., description="Your JWT Token"),
    db: AsyncSession = Depends(get_async_session)
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could Not Validate Credentials!"
    )
    
    try:
        payload = jwt.decode(x_token, SECRET_KEY, ALGORITHM)
        user_id: str = payload.get('sub') #type:ignore
        if user_id is None:
            raise credential_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired!"
        )
    except jwt.InvalidTokenError:
        raise credential_exception
    
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if user is None:
        raise credential_exception
    
    return user

async def update_user_service(
    current_user: User,
    fullname: str | None,
    profile_image: UploadFile | None,
    db: AsyncSession
):
    if fullname is not None:
        current_user.fullname = fullname #type:ignore
    
    if profile_image is not None:
        cloudinary_response = await upload_image(profile_image)
        current_user.profile_image_url = cloudinary_response.get('secure_url')
    
    await db.commit()
    await db.refresh(current_user)
    
    return current_user

async def delete_user_service(
    current_user: User,
    db: AsyncSession
):
    query = select(Post).where(Post.user_id == current_user.id)
    result = await db.execute(query)
    user_posts = result.scalars().all()
    
    for post in user_posts:
        if post.url: #type:ignore
            await delete_image(post.url) #type:ignore
    if current_user.profile_image_url: #type:ignore
        await delete_image(current_user.profile_image_url) #type:ignore
    
    await db.delete(current_user)
    await db.commit()
    
    return {
        "message": "User account and all associated media files deleted successfully"
    }