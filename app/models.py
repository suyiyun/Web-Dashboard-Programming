from sqlalchemy import Column, Float, String, Integer, Numeric
from .database import Base
class salary(Base):
    tablename = "salary"
    id = Column(Integer, primarykey=True, index=True)
    player = Column(String, unique=True, index=True)
    fieldposition = Column(String)
    team = Column(String)
    salary = Column(Numeric)
