from pydantic import BaseModel, Date
from typing import Optional

class ExpenseBase(BaseModel):
    amount: float
    date: Date  # ISO format date string
    source: str
    is_recurring: bool

class ExpenseUpdate(BaseModel):
    amount: Optional[float] 
    date: Optional[Date]  # ISO format date string
    source: Optional[str]
    is_recurring: Optional[bool] = False  

class ExpenseDisplay(BaseModel):
    amount: Optional[float] 
    date: Optional[Date]  # ISO format date string
    source: Optional[str]
    is_recurring: Optional[bool] = False  
    id:int
    user_id:int