"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Heart Attack Prediction Model")

    # Add image to the home page
    st.image("./images/home.jpeg")

    st.radio()
    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Cardiovascular disease remains one of the leading causes of death worldwide, that claimed over 17.9 million lives in 2019, representing 32% of all global deaths. Of these deaths, 85% were due to heart attack and stroke. Every year about 805,000 Americans have a heart attack. Of these, 605,000 are a first heart attack and 200,000 happen in people who have already experienced a heart attack.  In addition to being considered the leading cause of morbidity in the US, Cardiovascular disease and strokes are important drivers of US health care costs, accounting for $251 billion in health care spending in 2019. However AI prediction, awareness and diagnostic tools are turning the page in healthcare. Due to Artificial Intelligence, the convergence of technology and medicine has a bright and promising future, where innovation isn't just improving lives, it's saving them too.
    
        </p>
    """, unsafe_allow_html=True)

    import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    name = st.text_input('Name', on_change=set_state, args=[2])

if st.session_state.stage >= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write(f':{color}[Thank you!]')
    st.button('Start Over', on_click=set_state, args=[0])