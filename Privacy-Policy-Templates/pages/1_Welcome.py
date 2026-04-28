# Landing Welcome page
#
# NOTE!
# THIS CODE HAS BEEN PORTED TO PAGES/1_Welcome.py
# We'll keep it in the repository for now as reference
import streamlit as st
import ollama
import json
import re


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
                This tool is designed to help you easily understand privacy policies by introducing <i>consistency</i> into the process!
            </p>
            """, unsafe_allow_html=True)


def privacy_policy_summary(privacy_policy_text, client):
    model_name = "privacy-policy-summarizer"
    
    prompt = f"""
You are a strict privacy policy analysis engine.

Step 1: Read and understand the policy.
Step 2: Create a concise internal summary.
Step 3: Convert it into JSON.

Return ONLY valid JSON.

FORMAT:
{{
    "data_collection": "",
    "data_usage": "",
    "third_party_sharing": "",
    "user_rights": "",
    "security": "",
    "key_risks": ""
}}

RULES:
- No text outside JSON
- No markdown
- No missing keys
- If unknown, write "Not specified"

Privacy Policy:
{privacy_policy_text}
"""

    response = client.generate(
        model=model_name,
        prompt=prompt
    )

    raw = response["response"]

    # Extract JSON safely
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    cleaned = match.group(0) if match else raw

    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        parsed = {}

    # Enforce schema
    required_keys = [
        "data_collection",
        "data_usage",
        "third_party_sharing",
        "user_rights",
        "security",
        "key_risks"
    ]

    for key in required_keys:
        if key not in parsed or not parsed[key]:
            parsed[key] = "Not specified"

    return parsed


def main():
    st.set_page_config(page_title="Privacy Policy Summarizer")

    st.title("Privacy Policy Summarizer")

    if "done" not in st.session_state:
        st.session_state.done = False
    if "summary" not in st.session_state:
        st.session_state.summary = {}

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

        st.session_state.summary = summary
        st.session_state.done = True

    if st.session_state.done:
        st.subheader("Summary")
        st.json(st.session_state.summary)

        # Navigation buttons
        if st.button("Nutrition Label", type="primary"):
            st.switch_page("pages/2_Nutrition_Label_Template.py")

        if st.button("Tabular Format", type="primary"):
            st.switch_page("pages/3_Tabular_Format_Template.py")


if __name__ == "__main__":
    main()