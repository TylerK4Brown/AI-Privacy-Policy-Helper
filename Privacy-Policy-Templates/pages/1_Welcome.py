import streamlit as st
import ollama
import json
import re
from typing import List, Dict

# ---------------- CONFIG ---------------- #

MODEL_NAME = "privacy-policy-summarizer"

FIELDS = {
    "data_collection": (
        "Identify all explicitly mentioned types of personal data collected. "
        "Include identifiers (name, email), contact info, payment data, device data, "
        "browsing activity, location data, audio/video, and inferred data. "
        "Do NOT infer or guess."
    ),
    "data_usage": (
        "Identify all explicitly stated purposes for using collected data. "
        "Include marketing, advertising, analytics, personalization, service improvement, "
        "fraud prevention, or account functionality."
    ),
    "third_party_sharing": (
        "State whether data is shared with third parties. "
        "List who it is shared with and why if mentioned. "
        "If not mentioned, return 'Not specified'."
    ),
    "user_rights": (
        "List all explicitly stated user rights including access, deletion, correction, "
        "opt-out, portability, and consent withdrawal."
    ),
    "security": (
        "Extract all explicit statements about data security protections. "
        "Include encryption, storage, access controls, audits, breach response."
    ),
    "key_risks": (
        "Identify only explicit privacy risks implied by the policy. "
        "Do NOT speculate."
    )
}


# ---------------- UI ---------------- #

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
""", unsafe_allow_html=True)

# ---------------- JSON PARSER ---------------- #

def extract_json(raw: str):
    try:
        return json.loads(raw)
    except:
        match = re.search(r"\{[\s\S]*\}", raw)
        if match:
            try:
                return json.loads(match.group(0))
            except:
                return None
    return None

# ---------------- SECTION DETECTION ---------------- #

def split_into_sections(text: str):
    pattern = r"(data collection|information we collect|how we use|usage|sharing|third parties|cookies|security|your rights|retention|contact)"

    lines = text.split("\n")

    sections = {}
    current = "general"
    sections[current] = []

    for line in lines:
        clean = line.strip()
        lower = clean.lower()

        if re.search(pattern, lower) and len(clean.split()) <= 10:
            current = lower
            sections[current] = []
        else:
            sections[current].append(clean)

    return {
        k: "\n".join(v).strip()
        for k, v in sections.items()
        if "\n".join(v).strip()
    }

# ---------------- SECTION ANALYSIS ---------------- #

def analyze_section(name: str, text: str):

    text = text.encode("utf-8", "ignore").decode("utf-8")

    prompt = f"""
You are a strict privacy policy extraction engine.

Analyze ONLY this section: {name}

Return ONLY valid JSON:

{{
  "data_collection": "",
  "data_usage": "",
  "third_party_sharing": "",
  "user_rights": "",
  "security": "",
  "key_risks": ""
}}

Rules:
- Only explicit information
- No guessing
- If missing: "Not specified"
- No explanation or markdown

TEXT:
{text}
"""

    try:
        response = ollama.generate(
            model=MODEL_NAME,
            prompt=prompt
        )

        raw = response.get("response", "")
        parsed = extract_json(raw)

        if not parsed:
            parsed = {}

        for k in FIELDS:
            parsed.setdefault(k, "Not specified")

        return parsed

    except Exception:
        return {k: "Error in section" for k in FIELDS}

# ---------------- CLEAN MERGE (FIXED OUTPUT) ---------------- #

def merge_results(results: List[Dict]) -> Dict:
    combined = {k: [] for k in FIELDS}

    for r in results:
        for k in FIELDS:
            val = r.get(k)
            if val and val != "Not specified" and "Error" not in val:
                combined[k].append(val)

    cleaned = {}

    for k, values in combined.items():
        unique_values = list(dict.fromkeys(values))

        if not unique_values:
            cleaned[k] = "Not specified"
        else:
            cleaned[k] = " ".join(
                [v.strip().rstrip(".") + "." for v in unique_values]
            )

    return cleaned

# ---------------- PIPELINE ---------------- #

def analyze_policy(text: str):
    sections = split_into_sections(text)

    st.write(f"📄 Detected {len(sections)} sections")

    results = []

    for i, (name, content) in enumerate(sections.items()):
        with st.spinner(f"Analyzing section {i+1}/{len(sections)}: {name[:40]}..."):
            results.append(analyze_section(name, content))

    return merge_results(results)

# ---------------- MAIN APP ---------------- #

def main():

    if "summary" not in st.session_state:
        st.session_state.summary = {}

    text = st.text_area("Paste Privacy Policy:", height=300)

    if st.button("Generate Summary"):
        if not text.strip():
            st.warning("Please enter a privacy policy first.")
            return
        st.session_state.summary = analyze_policy(text)

    if st.session_state.summary:
        st.subheader("Structured Summary")
        st.json(st.session_state.summary)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Nutrition Label"):
                st.switch_page("pages/2_Nutrition_Label_Template.py")

        with col2:
            if st.button("Tabular Format"):
                st.switch_page("pages/3_Tabular_Format_Template.py")


if __name__ == "__main__":
    main()