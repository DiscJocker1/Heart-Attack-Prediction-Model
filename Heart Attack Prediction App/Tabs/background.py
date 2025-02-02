"""This modules contains data about my project"""

import streamlit as st

option = st.selectbox(
    "My Project INFO",
    ("Background Information", "Problem", "Solution", "Why I did this", "Methodology"),
)

st.write("You selected:", option)