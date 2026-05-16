from pydantic import BaseModel
from typing import Optional
from datetime import date
class IncomeBase(BaseModel):
    amount: float = None
    date: date = None # ISO format date string
    source: str= None
    is_recurring: bool= None

class IncomeUpdate(BaseModel):
    amount: Optional[float] = None
    date: Optional[date] = None # ISO format date string
    source: Optional[str]= None
    is_recurring: Optional[bool] = None  

class IncomeDisplay(BaseModel):
    amount: Optional[float] 
    date: Optional[date]  # ISO format date string
    source: Optional[str]
    is_recurring: Optional[bool] = False  
    id:int
    user_id:int
    