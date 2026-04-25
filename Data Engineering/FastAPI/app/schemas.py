from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PostCreate(BaseModel):
    caption: Optional[str]
    
class PostResponse(BaseModel):
    id: str
    caption: Optional[str]
    url: str
    file_type: str
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
    
class UserResponse(BaseModel):
    id: str
    fullname: str
    email: str
    profile_image: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attribute = True
        
class Token(BaseModel):
    access_token: str
    token_type: str