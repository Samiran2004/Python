
import os

import cloudinary
from dotenv import load_dotenv
from fastapi import HTTPException, UploadFile, status
from cloudinary.uploader import upload, destroy

load_dotenv()

cloudinary.config(
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key = os.getenv("CLOUDINARY_API_KEY"),
    api_secret = os.getenv("CLOUDINARY_API_SECRET")
)

async def upload_image(image: UploadFile):
    try:
        upload_result = upload(image.file)
        return upload_result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error uploading file: {e}")

async def extract_public_id(url: str):
    """
    Safely extracts the Cloudinary public_id from a secure URL.
    """
    try:
        parts = url.split('/upload/')
        if len(parts) > 1:
            path_part = parts[1]

            # Cloudinary version tags are 'v' followed by numbers (e.g., v171242312)
            first_segment = path_part.split('/')[0]
            if path_part.startswith('v') and first_segment[1:].isdigit():
                # Strip out the version tag
                path_part = path_part.split('/', 1)[1]
            public_id = path_part.rsplit('.', 1)[0]
            return public_id
    except Exception as e:
        print(f"Error parsing URL {url}: {e}")
    return None

async def delete_image(url: str):
    if not url:
        return
    public_id = extract_public_id(url=url)
    if public_id:
        try:
            is_video = url.lower().endswith((".mp4", ".mov", ".avi", ".mkv", ".webm"))
            res_type = "video" if is_video else "image"

            # Send the destroy command
            response = destroy(public_id, resource_type=res_type)

            # Print Cloudinary's exact response!
            print(f"✅ Cloudinary Response for {public_id}: {response}")
        except Exception as e:
            print(f"Failed to delete {public_id} from Cloudinary: {e}")