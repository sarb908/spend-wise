from jose import jwt,JWTError
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models.user import DbUser
from auth_token import oauth2_scheme
SECRET_KEY = 'LKAJFDLKJSLKFJLS'
ALGORITHIM = 'HS256'



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