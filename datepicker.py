import streamlit as st
from datetime import datetime

# Streamlit app layout
st.title("Date Picker")

# Date picker widget
selected_date = st.date_input("Select a date", datetime.now())

# Display the selected date
st.write(f"Selected date: {selected_date.strftime('%Y-%m-%d')}")
