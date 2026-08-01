from datetime import date 
from pydantic import BaseModel, Field

#EXPENSECREATE (USED WHEN CLIENT SENDS A NEW EXPENSE)
class ExpenseCreate(BaseModel):
   title: str = Field(min_length=1,max_length=100)
   amount: float = Field(gt=0)
   category: str = Field(min_length=1,max_length=100)
   date:date

class Expense(ExpenseCreate):
   id:str
   