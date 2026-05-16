from database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date, Boolean, Float



class DbExpense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    category = Column(String, nullable=False)
    is_recurring = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)