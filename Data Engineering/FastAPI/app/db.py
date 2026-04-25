import uuid
from collections.abc import AsyncGenerator

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, CHAR
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func

# 1. Using the verified TCP connection string
# Updated to 127.0.0.1 as your previous logs showed successful pings here
DATABASE_URL = "mysql+aiomysql://root:200430@127.0.0.1:3306/FastAPI"

# 2. Setup Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "Posts"
    
    id = Column(
        CHAR(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
        # FIX: Removed autoincrement=True because UUIDs are strings, not integers!
    )
    caption = Column(Text)
    url = Column(String(255), nullable=False) 
    file_type = Column(String(50), nullable=False)
    
    user_id = Column(
        CHAR(36),
        ForeignKey("Users.id", ondelete="CASCADE"),
        nullable=False
    )
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
class User(Base):
    __tablename__ = "Users"
    
    id = Column(
        CHAR(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    
    fullname = Column(
        String(100),
        nullable=False
    )
    
    email = Column(
        String(150),
        nullable=False,
        unique=True,
        index=True
    )
    
    hashed_password = Column(
        String(255),
        nullable=False
    )
    
    profile_image_url = Column(
        String(255),
        nullable=True
    )
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
async def create_db_and_tables():
    async with engine.begin() as conn:
        # This will now succeed because String has a defined length
        await conn.run_sync(Base.metadata.create_all)

# 3. Dependency for FastAPI endpoints
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
