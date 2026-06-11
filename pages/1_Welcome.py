# Landing Welcome page
import streamlit as st
import ollama
import pages.llm_functions as llm_functions

# Instantiate the Ollama client
client = ollama.Client()

# Introductory text for the landing page
st.markdown("""
            <h1 style='text-align: center;'>
                Welcome to the AI Privacy Policy Helper!
            </h1>
            
            <h6 style='text-align: center;'>
                The name is a work in progress...
            </h6>
            
            <h2 style='text-align: center;'>
                Developers: Tyler Brown & Lillian Brooks
            </h2>
            
            <p style='text-align: center; font-size: 20px;'>
                This tool is designed to help you easily understand privacy policies by introducing <i>consistency</i> into the process! <br /><br />
                Enter the text of any privacy policy, and our AI model will generate a concise summary of the most important information.<br /><br />
                This summary will then be used to generate a webpage template to view that information in a more digestible format.<br /><br />
                <b>This webpage template will be the same for every privacy policy</b>, so you can always know where to find the information you care about.
            </p>
            <br />
            """, unsafe_allow_html=True)

# Text area for the user to input the privacy policy text
privacy_policy_text = st.text_area(
    "Paste the privacy policy text below:",
    height=300
)

# Create columns so that the "Generate Summary" button is centered
left, middle, right = st.columns(3)

# Instantiate session state variables for state checking down the line
# Also allows for information to be accessed in the webpage template pages
if "summary" not in st.session_state:
    st.session_state.summary = None
    st.session_state.webpage_json = {}

# Session state that disables the button while a summary is being generated
# Starts off enabled so the user can generate a summary
if "disabled_summary_button" not in st.session_state:
    st.session_state.disabled_summary_button = False

# Function that is called on click of the "Generate Summary" button, disables the button
def click_generate_summary():
    st.session_state.disabled_summary_button = True

# Generates privacy policy text and stores it in the session state
middle.button("Generate Summary", on_click=click_generate_summary, disabled=st.session_state.disabled_summary_button, width=700, type="primary")

if st.session_state.disabled_summary_button:
    if not privacy_policy_text.strip():
        st.warning("Please enter some text first.")
        st.stop()

    # Reset the webpage JSON if a new summary is being generated
    if len(st.session_state.webpage_json) > 0:
        st.session_state.webpage_json = {}

    # Disable the summary button and generate a summary if text was input into the text area
    # Store the summary in the session state
    st.session_state.disabled_summary_button = True
    with st.spinner("Generating summary..."):
        st.session_state.summary = llm_functions.privacy_policy_summary(privacy_policy_text, client)

# Only display a summary if the json_generated session state flag is true
if st.session_state.summary:
    st.subheader("Summary")
    st.json(st.session_state.summary)

# If the summary was generated and the webpage JSON hasn't been generated yet, generate the webpage JSON and store it in the session state
if st.session_state.summary and len(st.session_state.webpage_json) == 0:
    with st.spinner("Generating webpage JSON..."):
        st.session_state.webpage_json = llm_functions.webpage_generator(st.session_state.summary, client)

# If the webpage JSON was generated, display it on screen for testing
if len(st.session_state.webpage_json) > 0:
    st.subheader("Generated Webpage JSON")
    st.json(st.session_state.webpage_json)
    # Enable the summary button again
    # The button only enables after the user navigates to the webpage template and comes back, which is a bit clunky but it works for now
    st.session_state.disabled_summary_button = False

# Create new columns down here so that the "Go to Nutrition Label" button is centered as well
left_1, middle_1, right_1 = st.columns(3)

# Navigation button to the webpage
if middle_1.button("Go to Nutrition Label ➡", type="secondary", width=700):
    st.switch_page("pages/2_Nutrition_Label_Template.py")