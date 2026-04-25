from datetime import datetime, timedelta, timezone
import jwt
import bcrypt

# --- JWT Configuration ---
# In a real app, store this SECRET_KEY in your .env file!
SECRET_KEY = "super_secret_key_change_this_in_production" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 # 24 hours

# --- Password Hashing ---
def get_password_hash(password: str) -> str:
    """Hashes a plain-text password using pure bcrypt."""
    # bcrypt requires bytes, so we encode the string
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    
    # Return the string representation for the database
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain-text password against the hashed version."""
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    
    return bcrypt.checkpw(password_byte_enc, hashed_password_bytes)

# --- JWT Generation ---
def create_access_token(data: dict):
    """Generates a JSON Web Token (JWT)."""
    to_encode = data.copy()
    
    # Calculate the expiration time
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Generate the JWT string
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt