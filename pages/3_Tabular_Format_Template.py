# ---- NOTE ----
# This page is not completed. It's a template for a potential future page that would present the summary in a tabular format.
# This would give the user options as to how they would like their summary to be presented

# Tabular Format Template page
# We'll try to recreate the typical financial institution privacy policy tables
# Something like this would be acceptable: https://www.consumerfinance.gov/rules-policy/regulations/1016/a/#ImageA1b
import streamlit as st

# Check to see if a user generated a summary yet
# If not, ask them to go back and generate one
summary = st.session_state.get("summary", None)
st.title("Privacy Policy Tabular Format")

if not summary:
    st.warning("No summary found. Please go back and generate one first.")
    st.stop()

# Table dictionary to pass into st.table
# Follows a very similar format to the nutrition label page
# Main difference lies in its structure, more tabular + less focused on design
table_format = {
    "Data Type": [
        "🔒 Data privacy", 
        "🔍 Data collection", 
        "🔗 Third-Party Sharing",
        "🛡️ Security",
        "⚖️ User Rights",
        "⚠️ Key Risks"],
    
    "Description": [
        "Information about how your data is protected and used", 
        "Information about what data is collected and how it's collected", 
        "Information shared with third parties",
        "Information about the security measures in place to protect your data",
        "Information about your rights regarding your data",
        "Information about potential risks associated with your data"],
    
    "Purpose": [
        # Data Privacy
        f'''- {summary.get("data_usage", "Not specified")}''',
        # Data Collection
        f'''- {summary.get("data_collection", "Not specified")}''',
        # Third-Party Sharing
        f'''- {summary.get("third_party_sharing", "Not specified")}''',
        # Security
        f'''- {summary.get("security", "Not specified")}''',
        # User Rights
        f'''- {summary.get("user_rights", "Not specified")}''',
        # Key Risks
        f'''- {summary.get("key_risks", "Not specified")}''']
}

st.table(table_format, height='content')
if st.button("⬅ Back", type="secondary"):
    st.switch_page("pages/1_Welcome.py")


