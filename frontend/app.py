import streamlit as st
from add_or_update import add_or_update_tab
from analytics_category import analytics_category_tab
from analytics_months import analytics_months_tab


st.title("Expense Management System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Month"])

with tab1:
    add_or_update_tab()
with tab2:
    analytics_category_tab()
with tab3:
    analytics_months_tab()
