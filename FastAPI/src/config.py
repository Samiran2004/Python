from pydantic_settings import BaseSettings
import os
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str
    VERSION: str
    DESCRIPTION: str
    DATABASE_URL: str

    class Config:
        env_file = os.path.join(Path(__file__).parent, ".env")

settings = Settings() # type: ignore
