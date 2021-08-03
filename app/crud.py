from sqlalchemy.orm import Session
from .import models
def getsalary(db: Session):
    returndb.query(models.salary.player, models.salary.fieldposition, models.salary.team).all()
