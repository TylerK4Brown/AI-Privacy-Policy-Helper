# Landing page for our privacy policy templage playground
# Small description of the website in HTML

import streamlit as st

st.markdown("""
            <h1 style='text-align: center;'>
                Welcome to the AI Privacy Policy Helper!</h1>
            
            <p style='text-align: center; font-size: 20px;'>
                This page houses the templates fed into our AI models that attempt to achieve this goal. <br />
            </p>
            
            <h3 style='text-align: center'>
               Once the "Privacy Policy Templates" tab pops check out the privacy policy in different formats 
            </h3>
          
          """, unsafe_allow_html=True)
