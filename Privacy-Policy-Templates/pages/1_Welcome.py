# Landing page for our privacy policy templage playground
# Small description of the website in HTML

import streamlit as st

st.markdown("""
            <h1 style='text-align: center;'>
                Welcome to the AI Privacy Policy Helper!
            </h1>
            
            <h6 style='text-align: center;'>
                The name is a work in progres...
            </h6>
            
            <h2 style='text-align: center;'>
                Developers: Tyler Brown & Lillian Brooks
            </h2>
            
            <p style='text-align: center; font-size: 20px;'>
                This tool is designed to help you easily understand privacy policies by introducing <i>consistency</i> into the process! <br />
                This page houses the templates fed into our AI models that attempt to achieve this goal. <br />
            </p>
            
            <h3 style='text-align: center'>
                Click on "Privacy Policy Templates" at the top to see these templates in action!
            </h3>
          
          """, unsafe_allow_html=True)
