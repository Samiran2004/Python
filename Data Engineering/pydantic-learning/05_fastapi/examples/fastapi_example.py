from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Settings(BaseModel):
    app_name: str = "FastAPI Basic"
    admin_email: str = "samiran123@gmail.com"
    
def get_app_settings():
    return Settings()

@app.post('/signup')
def signup(user: UserSignup):
    return {
        'message': f"User: {user.username}, signed up successfully"
    }

@app.get('/settings')
def get_settings(settings: Settings = Depends(get_app_settings)):
    return settings