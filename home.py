# Page configuration initialization for our privacy policy template 'playground'
# This will be a small website that we can access to test our privacy policy templates/refine the code of them
import streamlit as st

# Initialize the page configuration for the application
st.set_page_config(
    page_title="AI Privacy Policy Helper"
)
# Stretches the text out so that it fits most of the page
st.set_page_config(layout="wide")

# Page layout
# Dictionary of lists, each list containing a section name and its corresponding page path.
# this is displayed at the top of the screen
pages = {
    "Introduction": [
        st.Page("pages/1_Welcome.py", title='Privacy Policy Summarizer')
    ],
    "Privacy Policy Templates": [
        st.Page("pages/2_Nutrition_Label_Template.py"),
        st.Page("pages/3_Tabular_Format_Template.py")
    ],
}

# Instantiates the navigation so it can be displayed on the landing page
pg = st.navigation(pages, position='top')
pg.run()