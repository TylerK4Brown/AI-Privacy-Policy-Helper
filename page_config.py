# Page configuration initialization for our privacy policy template 'playground' 
# This will be a small website that we can access to test our privacy policy templates/refine the code of them 
import streamlit as st 
# Initialize the page configuration for the application 
st.set_page_config( 
 page_title="AI Privacy Policy Helper",
 # Stretches the text out so that it fits most of the page
  layout="wide" 
  )

# Navigation structure
pages = {
    "Introduction": [
        st.Page("pages/Welcome.py", title="Privacy Policy Summarizer")
    ],
    "Privacy Policy Templates": [
        st.Page("pages/1_Nutrition_Label_Template.py", title="Nutrition Label"),
        st.Page("pages/2_Tabular_Format_Template.py", title="Tabular Format")
    ]
}

# Create and run navigation
pg = st.navigation(pages, position='top')
pg.run() 