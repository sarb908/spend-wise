from fastapi import APIRouter, Depends
from models.income import DbIncome
from schema import income
from sqlalchemy.orm import Session
from sqlalchemy import func
from schema.income import IncomeBase, IncomeDisplay, IncomeUpdate
from dependencies import get_current_user
from database import get_db
from auth_token import oauth2_scheme
from db.db_income import create_income, get_income,update_income


income_router = APIRouter(prefix="/income", tags=["incomes"])

@income_router.post("/")
def create(request: IncomeBase,token: str = Depends(oauth2_scheme),  db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    print("current_user",current_user.username, current_user.email, current_user.id)
    print(current_user.id)
    create_in= create_income(request, db, current_user )
    return create_in


@income_router.get("/", response_model=list[IncomeDisplay])
def get_incomes(source: str = None, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    incomes = get_income(source, db, current_user)
    return incomes  


@income_router.get("/total-income")
def get_total_income(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    total_income = (
        db.query(func.sum(DbIncome.amount))      # SELECT SUM(amount)
        .filter(DbIncome.user_id == current_user.id)  
        .scalar()                               
    ) or 0
    return {"total_income": total_income}


@income_router.patch("/{income_id}")
def update_income(income_id: int, request: IncomeUpdate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    income = update_income(income_id, request, db, current_user)
    return income


@income_router.delete("/{income_id}")
def delete_income(income_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    income = db.query(DbIncome).filter(DbIncome.id == income_id, DbIncome.user_id == current_user.id).first()
    if not income:
        return {"error": "Income not found"}
    db.delete(income)
    db.commit()
    return {"message": "Income deleted successfully"}