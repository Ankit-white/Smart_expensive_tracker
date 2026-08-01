# AI Notes

## 1. What was done by AI-generated and what was written by me
Project scaffolding (folders structure, requirements.txt) – AI-generated, used as is
Expense data model – AI-generated, with minor adjustments to add validation of negative amounts and date format
CRUD endpoints – first draft provided by AI, error handling rewritten by me
Category summary logic – AI-generated, cross-validated totals with manual calculation
Tests – initial set provided by AI, added a few more test cases myself
README – written by me, with minor adjustments from AI to improve formatting

## 2. What was validated/tested/refactored by me and why
I cross-validated category totals by manually calculating the expected totals for three expenses in two categories before trusting the automated tests.
I re-ran the installation, start, and test commands from README to ensure that they work on a fresh clone of the repository.
Set up the project and development environment locally.
Fixed the expense creation bug in the storage logic.
Executed the complete test suite and resolved issues untill all tests passed sucessfully
