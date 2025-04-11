"""This module contains data for the About page"""

# Import necessary modules
import streamlit as st
from PIL import Image

def app():
    """This function creates the About page"""
    
    # Display balloons for a fun effect
    st.balloons()

    # Page Title
    st.title('About')

    # Embed the CodePen Animation
    codepen_embed_url = "https://codepen.io/alexandrevacassin/full/MYgNEQW"  # Full view link

    st.markdown(
        f'''
        <div style="text-align: center;">
            <iframe src="{codepen_embed_url}" width="100%" height="700px" style="border:none;"></iframe>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Contact Information
    st.markdown("### Name: KK")
    st.markdown("### GitHub: [KK](https://github.com/DiscJocker1)")

    # Additional Information
    st.markdown(
        """<p style="font-size:18px;">
                What This App Does
            </p>
        """, unsafe_allow_html=True)
    
    st.markdown(
        """<p style="font-size:18px;">
                This app leverages Deep learning and AI to predict heart attack risks. 
                My mission is to empower individuals with **early intervention, prediction and detection** for better cardiac health.
            </p>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center;">Built with ❤️ by a passionate cardiac researcher.</p>',
        unsafe_allow_html=True
    )