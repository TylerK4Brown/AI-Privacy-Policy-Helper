# Nutrition Label Template page
# Uses streamlit_extras to create a Nutrition Label-esc template for the user's summarized privacy policy
# Rough draft at the moment, and will need a great deal of refining
import streamlit as st
from streamlit_extras.grid import grid

st.set_page_config(page_title="Nutrition Label")
st.title("Privacy Policy Nutrition Label")

summary = st.session_state.get("summary", None)

if not summary:
    st.warning("No summary found. Please go back and generate one first.")
    st.stop()
# Assigns a grid layout to the page
# First column has only 1 cell, second column has two cells, and the third column has 1 cell
grid_example = grid(1, 2, 1, vertical_align="top")

# Expander function creates a collapsible section in the streamlit app, which is useful for organizing content 
# It also formats the content in a nice format that follows quite closely to the nutriton label format
#🔒 Data privacy
with grid_example.expander("🔒 Data privacy", expanded=True):
    # Use HTML in st.markdown to display the content
    # It's considered "unsafe" due to cross-site scripting attacks
    # ^^^ We're not using any user input in this HTML, so we won't have to worry about this
    # This applies to all columns that are created
    st.markdown(f"""
                <h1 style='text-align: center;'>
                    <u>Nutrition Label Template</u>
                </h1>
                 <p style='text-align: center; font-size: 15px;'>
            {summary.get("data_usage", "Not specified")}
        </p
                """, unsafe_allow_html=True)
 #🔍 Data collection
with grid_example.expander("🔍 Data collection", expanded=True):
    st.markdown(f"""
                 <h2 style='text-align: center;'><u>Data Collection</u></h2>
        <p style='text-align: center; font-size: 15px;'>
            {summary.get("data_collection", "Not specified")}
        </p>

            """, unsafe_allow_html=True)

        
# 🔗 Third Party Sharing
with grid_example.expander("🔗 Third Party Sharing", expanded=True):
    st.markdown(f"""
        <h2 style='text-align: center;'><u>Third Party Sharing</u></h2>
        <p style='text-align: center; font-size: 15px;'>
            {summary.get("third_party_sharing", "Not specified")}
        </p>
    """, unsafe_allow_html=True)


# 🛡️ Security
with grid_example.expander("🛡️ Security", expanded=True):
    st.markdown(f"""
        <h2 style='text-align: center;'><u>Security</u></h2>
        <p style='text-align: center; font-size: 15px;'>
            {summary.get("security", "Not specified")}
        </p>
    """, unsafe_allow_html=True)


# ⚖️ User Rights
with grid_example.expander("⚖️ Your Rights", expanded=True):
    st.markdown(f"""
        <h2 style='text-align: center;'><u>User Rights</u></h2>
        <p style='text-align: center; font-size: 15px;'>
            {summary.get("user_rights", "Not specified")}
        </p>
    """, unsafe_allow_html=True)


# ⚠️ Risks
with grid_example.expander("⚠️ Key Risks", expanded=True):
    st.markdown(f"""
        <h2 style='text-align: center;'><u>Key Risks</u></h2>
        <p style='text-align: center; font-size: 15px;'>
            {summary.get("key_risks", "Not specified")}
        </p>
    """, unsafe_allow_html=True)
if st.button("⬅ Back", type="secondary"):
    st.switch_page("pages/1_Welcome.py")