# Smart Expense Tracker API

A REST API for managing personal expenses, enabling users to add, view, filter by category, calculate totals, and delete expenses.

# What I've Done

- Create a CRUD API for storing and retrieving expenses with fields `id`, `title`, `amount`, `category`, `date`
- Implemented filters to search expenses by category
- Added endpoints to calculate total expenses overall and by category
- Used in-memory storage (data is lost when the server restarts)

Describe what you've done to implement the solution. This should probably include some details about what technologies you've used (e.g., "Built using FastAPI and Pydantic") and any additional features, if applicable.
# Technologies

- [ ] e.g. Python 3.11 + FastAPI
- [ ] e.g. pytest

# Structure
```

your-repo/
README.md
AI_NOTES.md
src/
tests/
```
# Installation

```bash
# example - substitute with actualinstallation instructions
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
# Running

```bash
# example - substitute with actual command
uvicorn src.main:app --reload
```

The API will be available at http://localhost:8000

# Tests
```bash
# example - substitute with actual command
pytest tests/
```

# Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/expenses` | Create an expense |
| GET | `/expenses` | Get all expenses |
| GET | `/expenses?category=food` | Get expenses by category |
| GET | `/expenses/total` | Calculate total expenses |
| GET | `/expenses/total?category=food` | Calculate total expenses by category |
| DELETE | `/expenses/{id}` | Delete expense by id |
Update this section to reflect your actual API endpoints.

# Notes

See `AI_NOTES.md` for details about how this project was built using an AI.