from fastapi import APIRouter, Depends, HTTPException
from models.expense import DbExpense
from schema import income
from sqlalchemy.orm import Session
from sqlalchemy import func
from schema.expense import ExpenseBase, ExpenseDisplay, ExpenseUpdate
from dependencies import get_current_user
from database import get_db
from auth_token import oauth2_scheme
from db.db_expense import create_expense


expense_router = APIRouter(prefix="/expense", tags=["expenses"])

@expense_router.post("/", response_model=ExpenseDisplay)
def create(request: ExpenseBase,token: str = Depends(oauth2_scheme),  db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    print("current_user",current_user.username, current_user.email, current_user.id)
    print(current_user.id)
    create_in= create_expense(request, db, current_user )
    return create_in

@expense_router.get("/", response_model=list[ExpenseDisplay])
def read_expenses(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    print("current_user",current_user.username, current_user.email, current_user.id)
    print(current_user.id)
    expenses = db.query(DbExpense).filter(DbExpense.user_id == current_user.id).all()
    return expenses


@expense_router.get("/total")
def get_total_expenses(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    total = db.query(func.sum(DbExpense.amount)).filter(DbExpense.user_id == current_user.id).scalar()
    return {"total": total}



@expense_router.patch("/{id}", response_model=ExpenseDisplay)
def update_expense(id: int, request: ExpenseUpdate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expense = db.query(DbExpense).filter(DbExpense.id == id, DbExpense.user_id == current_user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    if request.amount is not None:
        expense.amount = request.amount

    if request.date is not None:
        expense.date = request.date

    if request.source is not None:
        expense.source = request.source

    if request.is_recurring is not None:
        expense.is_recurring = request.is_recurring
    db.commit()
    db.refresh(expense)
    return expense


@expense_router.delete("/{id}")
def delete_expense(id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expense = db.query(DbExpense).filter(DbExpense.id == id, DbExpense.user_id == current_user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}      