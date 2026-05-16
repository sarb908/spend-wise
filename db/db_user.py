



from auth_utils import get_password_hash
from sqlalchemy.orm import Session

from models.user import DbUser
from schema.user import UserBase


def create_user(request: UserBase, db: Session):
    print(request.password, get_password_hash(request.password))
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def find_user(request: UserBase, db: Session):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user