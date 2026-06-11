# Nutrition Label Template page
# Uses streamlit_extras to create a Nutrition Label-esc template for the user's summarized privacy policy
# streamlit_extras provides collapsable elements and a grid layout, which are used to create the template
import streamlit as st
from streamlit_extras.grid import grid

# Page config, title of the page and the header
st.set_page_config(page_title="Nutrition Label")
st.title("Privacy Policy Nutrition Label", text_alignment="center")

# Pull the webpage JSON from the session state
web_json = st.session_state.get("webpage_json", None)

# If the webpage JSON isn't found in the session state, it means that the user hasn't generated a summary yet
# Display a warning and a button that takes the user back to the generation page
if not web_json:
    st.warning("No summary found. Please go back and generate one first.")
    left, middle, right = st.columns(3)
    if middle.button("Go back to Generate Summary page", type="secondary", width=700):
        st.switch_page("pages/1_Welcome.py")
    st.stop()

# Assigns a grid layout to the page
# First column has only 1 cell, second and third columns have two cells, and the fourth column has 1 cell
grid_layout = grid(1, 2, 2, 1, vertical_align="top")

# Iterate through the elements in the webpage JSON
# Creates an expander element for each section
for element in web_json['elements']:
    with grid_layout.expander(element['header'], expanded=True):
        # Subheader text elaborates on the content of the section
        st.markdown(f"<h3 style='text-align: center;'>{element['subheader']}</h3>", unsafe_allow_html=True)
        
        # Bullet points are created by splitting the content on newline characters (LLM is told to split bullet points with newline characters in the prompt engineering)
        # They are then displayed in a two-column format for spacing purposes
        for bullet_point in range(0, len(element['content'].split("\n")), 2):
            bullet_point_1 = element['content'].split("\n")[bullet_point]
            
            # Ensures that an index out of range error doesn't occur if the number of bullet points is odd
            if bullet_point + 1 < len(element['content'].split("\n")):
                bullet_point_2 = element['content'].split("\n")[bullet_point + 1]
            else:
                bullet_point_2 = ""
            
            # Print the bullet points in a two-column format using inline CSS styling
            # Creates a div with display flex and gap of 10px, each bullet point is in its own div with flex 1 to take up equal space
            # This implementation is a bit hacky but it allows for the bullet points to be displayed in a more compact and visually appealing way
            st.markdown(f"""
                <div style='display: flex; gap: 10px; text-align: center; font-size: 20px;'>
                    <div style='flex: 1;'>{bullet_point_1}</div>
                    <div style='flex: 1;'>{bullet_point_2}</div>
                </div>""", unsafe_allow_html=True)

# Navigation button to go back to the generation page
if st.button("⬅ Back", type="secondary"):
    st.switch_page("pages/1_Welcome.py")