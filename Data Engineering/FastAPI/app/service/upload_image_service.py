from fastapi import HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import Post

from ..libs.cloudinary import upload_image


async def upload_image_service(
    file: UploadFile,
    caption: str,
    db: AsyncSession
):
    cloudinary_response = await upload_image(file)
    
    secure_url = cloudinary_response.get("secure_url")
    file_format = cloudinary_response.get("format", "unknown")
    
    if not secure_url:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get url from cloudinary!")
    
    new_post = Post(
        caption = caption,
        url = secure_url,
        file_type = file_format
    )
    
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    
    return new_post