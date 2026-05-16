from database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship



class DbExpense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    source = Column(String, nullable=False)
    is_recurring = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    
    user = relationship("DbUser", back_populates="expenses")