from datetime import datetime, timedelta,timezone
from jose import jwt,JWTError
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
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



def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(get_db)):


    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Credentials',
        headers={'WWW-Authenticate':'Bearer'}
    )

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHIM)
        username : str =  payload.get("sub")

        if not username:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    
    user = db.query(DbUser).filter(DbUser.username == username).first()

    if user is None:
        raise credentials_exception
    return user

