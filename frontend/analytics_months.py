import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    year = st.text_input(label="Year")
    if st.button("Get Month Summary"):
        if not year.isdigit():
            st.error("Please enter a valid numeric year.")
            return
        response = requests.get(f"{API_URL}/analytics_by_month/", params={"year": int(year)})
        data = response.json()
        df = pd.DataFrame(list(data.items()), columns=["Month", "Total Expense"])
        st.bar_chart(df.set_index("Month"))

        df["Total Expense"] = df["Total Expense"].map("{:.2f}".format)
        st.table(df)
