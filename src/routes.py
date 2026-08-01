from fastapi import APIRouter, HTTPException
from .schemas import ExpenseCreate
from .storage import (
    add_expense,
    load_expenses,
    delete_expense,
    get_total,
)

router = APIRouter()

#ADDA NEW EXPENSE
@router.post("/expenses", status_code=201)
def create_expense(expense: ExpenseCreate):
    return add_expense(expense)

#EXPENSES ARE FILTERD BY CATEGORY
@router.get("/expenses")
def get_expenses(category: str | None = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses

#CALCULATE THE TOTAL EXPENSE BY AMOUNT
@router.get("/expenses/total")
def total_expenses(category: str | None = None):
    return {
        "category": category,
        "total": get_total(category),
    }

#DELETE AN EXPENSE USING  UNIQUE ID
@router.delete("/expenses/{expense_id}", status_code=204)
def remove_expense(expense_id: str):
    deleted = delete_expense(expense_id)

#RETUEN 404 IF THE EXPENSE IS DELETED
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")