import json
from pathlib import Path
from uuid import uuid4

DATA_FILE = Path(__file__).parent/"expenses.json"

#READ ALL EXPENSES FROM THE JSON FILE
def load_expenses():
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")

    if DATA_FILE.stat().st_size==0:
        DATA_FILE.write_text("[]")

    with open(DATA_FILE,"r")as file:
        return json.load(file)

#WRITES THE UPDATED LIST BACK TO FILE
def save_expenses(expenses):
    with open(DATA_FILE,"w")as file:
        json.dump(expenses,file,indent=4)

#CREATE A UUID AND SAVES A NEW EXPENSE
def add_expense(expense):
    expenses = load_expenses()

    new_expense = expense.model_dump(mode = "json")
    new_expense["id"] = str(uuid4())

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense

#REMOVE AN EXPENSE BY ID
def delete_expense(expense_id):
    expenses=load_expenses()

    update=[expense for expense in expenses if expense["id"]!=expense_id]

    if len(update)==len(expenses):
        return False
    
    save_expenses(update)
    return True

#CALCULATES THE TOTAL,OPTIONALLY FILTERD BY CATEGORY
def get_total(category=None):
    expenses=load_expenses()
    
    if category:
        expenses=[e for e in expenses if e["category"]==category]

    return sum(e["amount"] for e in expenses)
