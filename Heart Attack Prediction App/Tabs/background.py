"""This modules contains data about my project"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("My Prediction Model")

    # Add image to the home page
    st.image("./images/home.jpeg")

    st.radio()
    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Cardiovascular disease remains one of the leading causes of death worldwide, that claimed over 17.9 million lives in 2019, representing 32% of all global deaths. Of these deaths, 85% were due to heart attack and stroke. Every year about 805,000 Americans have a heart attack. Of these, 605,000 are a first heart attack and 200,000 happen in people who have already experienced a heart attack.  In addition to being considered the leading cause of morbidity in the US, Cardiovascular disease and strokes are important drivers of US health care costs, accounting for $251 billion in health care spending in 2019. However AI prediction, awareness and diagnostic tools are turning the page in healthcare. Due to Artificial Intelligence, the convergence of technology and medicine has a bright and promising future, where innovation isn't just improving lives, it's saving them too.
    
        </p>
    """, unsafe_allow_html=True)