from datetime import datetime, timedelta,timezone
from jose import jwt,JWTError
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from database import get_db
from models.user import DbUser


SECRET_KEY = 'LKAJFDLKJSLKFJLS'
ALGORITHIM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def create_token(data : dict, expires_delta : Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHIM)
    return encoded_jwt





