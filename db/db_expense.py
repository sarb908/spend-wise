from models.expense import DbExpense
from schema.expense import ExpenseBase
from sqlalchemy.orm import Session


def create_expense(request: ExpenseBase, db: Session, current_user):
    new_expense = DbExpense(
        amount=request.amount,
        source=request.source,
        date = request.date,
        is_recurring = request.is_recurring,
        user_id=current_user.id
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense  