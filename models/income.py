from database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, Date, Boolean
from sqlalchemy.orm import relationship


class DbIncome(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable = False)
    date = Column(Date, nullable = False)
    source = Column(String, nullable = False)
    is_recurring = Column(Boolean, nullable = False)
    user_id = Column(Integer, ForeignKey("users.id") , nullable=False, index=True)

    user = relationship("DbUser", back_populates="incomes")

