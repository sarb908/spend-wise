from pydantic import BaseModel
from typing import Optional
from datetime import date
class ExpenseBase(BaseModel):
    amount: float
    date: date  # ISO format date string
    source: str
    is_recurring: bool

class ExpenseUpdate(BaseModel):
    amount: Optional[float] =None
    date: Optional[date] = None  # ISO format date string
    source: Optional[str] = None
    is_recurring: Optional[bool] = None                                 

class ExpenseDisplay(BaseModel):
    amount: Optional[float] 
    date: Optional[date]  # ISO format date string
    source: Optional[str]
    is_recurring: Optional[bool] = False  
    id:int
    user_id:int