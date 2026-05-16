from models.user import DbUser
from sqlalchemy.orm import Session
from database import get_db
from fastapi import APIRouter, Depends
from schema.user import UserBase, UserDisplay
from db.db_user import create_user
from auth_token import create_token
from dependencies import get_current_user   
from auth_utils import verify_password
from fastapi.security import OAuth2PasswordRequestForm

router  = APIRouter(prefix = "/auth" )


@router.post("/signup")
def signup(request:UserBase ,db:Session = Depends(get_db) ):
        user = create_user(request, db)
        token  =create_token({"data":{"sub": user.username}})
        return {
                "access_token": token,
                "token_type": "bearer"
            }




@router.post("/login" )
def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):        
        username = form_data.username
        print(form_data)
        user = db.query(DbUser).filter(DbUser.username == username).first()
        status = verify_password(form_data.password, user.password)

        if not status or user is None:
            return {"error": "Invalid credentials"}
        token  =create_token({"data":{"sub": user.username}})
        return {
                "access_token": token,
                "token_type": "bearer"
            }
    
