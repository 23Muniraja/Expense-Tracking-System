# 💰 Expense Management System

This is a full-stack **Expense Management System** with:

- ✅ A **Streamlit frontend** for intuitive user interaction  
- ✅ A **FastAPI backend** for handling API logic and database operations  
- ✅ A **MySQL database** for persistent storage  
- ✅ Logging for debugging and traceability  

---

## 🗂 Project Structure

```
expense-management-system/
├── backend/
│   ├── server.py               # FastAPI backend
│   ├── db_helper.py            # Database interaction layer
│   └── logging_setup.py        # Logger configuration
├── frontend/
│   ├── app.py                  # Streamlit main app
│   ├── add_or_update.py        # Tab 1: Add/Update expenses
│   ├── analytics_category.py   # Tab 2: Analytics by category
│   └── analytics_months.py     # Tab 3: Monthly analytics
├── tests/
│   └── ...                     # Test cases (optional)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI backend server:
```bash
cd backend
uvicorn server:app --reload
```

> 📁 Make sure you're in the `backend/` folder when running the above command.

### 4. Run the Streamlit frontend:
```bash
cd ../frontend
streamlit run app.py
```

---

## 🚀 Features

- Add/Update Expenses by date  
- View Category-Wise Analytics (with percentage breakdown)  
- View Month-Wise Expense Trends (bar chart + table)  
- REST API Integration with FastAPI  
- MySQL backend for real-time data storage  
- Logging to `server.log` for backend traceability  

---

## 🔌 API Endpoints

| Method | Endpoint                    | Description                         |
|--------|-----------------------------|-------------------------------------|
| `GET`  | `/expenses/{expense_date}`  | Get all expenses for a given date   |
| `POST` | `/expenses/{expense_date}`  | Replace expenses for a given date   |
| `POST` | `/analytics/`               | Category summary for date range     |
| `GET`  | `/analytics_by_month/`      | Month-wise summary for a given year|

---

## 📝 Example

### Analytics by Month Endpoint
```http
GET /analytics_by_month/?year=2024
```

Returns:
```json
{
  "January": 2300,
  "February": 1800,
  ...
}
```

---

## 📌 Notes

- Ensure MySQL is running and the `expense_manager` database is created.  
- Update DB credentials in `db_helper.py` if needed.  
- Logs are saved to `backend/server.log`.  

---

## 🙌 Acknowledgments

Built using:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [MySQL](https://www.mysql.com/)
- [Python Logging](https://docs.python.org/3/library/logging.html)
- CodeBasics DS AI Bootcamp

---

## 📧 Contact

For questions or suggestions:  
**Muniraja M** | `23muniraja@gmail.com`