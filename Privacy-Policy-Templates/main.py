# NOTE!
# THIS CODE HAS BEEN PORTED TO PAGES/1_Welcome.py
# We'll keep it in the reposiory for now as reference

import streamlit as st
import ollama


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
            """, unsafe_allow_html=True)
def privacy_policy_summary(privacy_policy_text, client):
    privacy_policy_summarizer = "privacy-policy-summarizer"  # Model name
    
    response = client.generate(
        model=privacy_policy_summarizer,
        prompt=privacy_policy_text
    )
    
    return response["response"]  


def main():
    st.set_page_config(page_title="Privacy Policy Summarizer")

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
            return

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

      
        st.page_link("pages/1_Welcome.py", label="Go to Next Page")


if __name__ == "__main__":
    main()