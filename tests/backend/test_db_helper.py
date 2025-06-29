from backend import db_helper

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-01-01","2199-01-01")
    assert len(summary) == 0