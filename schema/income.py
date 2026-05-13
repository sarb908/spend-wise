from pydantic import BaseModel, Date
from typing import Optional

class IncomeBase(BaseModel):
    amount: float
    date: Date  # ISO format date string
    source: str
    is_recurring: bool

class IncomeUpdate(BaseModel):
    amount: Optional[float] 
    date: Optional[Date]  # ISO format date string
    source: Optional[str]
    is_recurring: Optional[bool] = False  

class IncomeDisplay(BaseModel):
    amount: Optional[float] 
    date: Optional[Date]  # ISO format date string
    source: Optional[str]
    is_recurring: Optional[bool] = False  
    id:int
    user_id:int
    