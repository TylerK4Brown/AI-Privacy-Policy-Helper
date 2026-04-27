# Landing Welcome page
#
# Our webpage will be responsible for:
# 1. Accepting user input for the privacy policy text
# 2. Calling upon the locally hosted LLM to generate a summary of the privacy policy text
# 3. Calling upon another LLM that will generate Streamlit code to display the summary in a user-friendly format
# 4. Pushing the generated Streamlit code into the appropriate page


import streamlit as st
import ollama


def privacy_policy_summary(privacy_policy_text, client):
    privacy_policy_summarizer = "privacy-policy-summarizer"  # Model name
    
    response = client.generate(
        model=privacy_policy_summarizer,
        prompt=privacy_policy_text
    )
    
    return response["response"]  

st.markdown("""
            <h1 style='text-align: center;'>
                Welcome to the AI Privacy Policy Helper!</h1>
                
            <h6 style='text-align: center;'>
                The name is a work in progres...
            </h6>
            
            <h2 style='text-align: center;'>
                Developers: Tyler Brown & Lillian Brooks
            </h2>
            
            <p style='text-align: center; font-size: 20px;'>
                This tool is designed to help you easily understand privacy policies by introducing <i>consistency</i> into the process! <br />
          
          """, unsafe_allow_html=True)

st.title("Privacy Policy Summarizer")

# Initialize session state
if "done" not in st.session_state:
    st.session_state.done = False
if "summary" not in st.session_state:
    st.session_state.summary = ""

# Text input box
privacy_policy_text = st.text_area(
    "Paste the privacy policy text below:",
    height=300
)

if st.button("Generate Summary"):
    if not privacy_policy_text.strip():
        st.warning("Please enter some text first.")

    with st.spinner("Generating summary..."):
        client = ollama.Client()
        summary = privacy_policy_summary(privacy_policy_text, client)

    # Save results in state
    st.session_state.summary = summary
    st.session_state.done = True

# Show summary if done
if st.session_state.done:
    st.subheader("Summary")
    st.write(st.session_state.summary)