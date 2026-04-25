from fastapi import Depends, FastAPI, APIRouter, File, Form, UploadFile

from ..db import get_async_session
from ..service.upload_image_service import upload_image_service
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix='/api/v1'
)

@router.post('/upload')
async def handle_upload(
    image: UploadFile = File(...),
    caption: str = Form(None),
    db: AsyncSession = Depends(get_async_session)
):
    return await upload_image_service(image, caption, db)