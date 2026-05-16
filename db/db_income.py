from database import get_db
from dependencies import get_current_user
from models.income import DbIncome
from models.user import DbUser
from schema.user import UserDisplay
from sqlalchemy.orm import Session
from typing import Optional
from schema.income import IncomeBase
from fastapi import  Depends


def create_income(request: IncomeBase, db: Session, current_user:DbUser):
    new_income =  DbIncome(
        amount=request.amount,
        date = request.date,
        source = request.source,
        is_recurring = request.is_recurring,
        user_id = current_user.id
    )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income




def get_income(source:Optional[str]=None, db: Session = Depends(get_db), current_user:DbUser = Depends(get_current_user)):
    if source:
        income = db.query(DbIncome).filter(DbIncome.source == source, DbIncome.user_id == current_user.id).all()
    else:
        income = db.query(DbIncome).filter(DbIncome.user_id == current_user.id).all()       
    return income


