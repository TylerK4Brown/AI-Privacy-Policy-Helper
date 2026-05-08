import streamlit as st
import ollama
import json
import re
from typing import List, Dict

# ---------------- CONFIG ---------------- #

MODEL_NAME = "privacy-policy-summarizer"

FIELDS = {
    "data_collection": "Identify all explicitly mentioned types of personal data collected.",
    "data_usage": "Identify all explicitly stated purposes for using collected data.",
    "third_party_sharing": "State whether data is shared with third parties.",
    "user_rights": "List all explicitly stated user rights.",
    "security": "Extract all explicit statements about data security protections.",
    "key_risks": "Identify only explicit privacy risks implied by the policy."
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

    sections = {}
    current = "general"
    sections[current] = []

    for line in text.split("\n"):
        clean = line.strip().lower()

        if re.search(pattern, clean) and len(clean.split()) <= 10:
            current = clean
            sections[current] = []
        else:
            sections[current].append(line.strip())

    return {
        k: "\n".join(v).strip()
        for k, v in sections.items()
        if "\n".join(v).strip()
    }

# ---------------- CHUNKING (WITH OVERLAP) ---------------- #

def chunk_text(text: str, max_chars: int = 3000, overlap: int = 300) -> List[str]:
    text = text.strip()
    if len(text) <= max_chars:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + max_chars

        if end < len(text):
            period = text.rfind(".", start, end)
            newline = text.rfind("\n", start, end)
            break_point = max(period, newline)

            if break_point > start + 500:
                end = break_point + 1

        chunks.append(text[start:end].strip())

        start = max(end - overlap, 0)

        if start >= len(text):
            break

    return chunks

# ---------------- MODEL CALL ---------------- #

def analyze_section(name: str, text: str):

    prompt = f"""
You are a strict privacy policy extraction engine.

Analyze ONLY this section: {name}

Return ONLY valid JSON with:
- data_collection
- data_usage
- third_party_sharing
- user_rights
- security
- key_risks

Rules:
- Only explicit info
- No guessing
- If missing: "Not specified"

TEXT:
{text}
"""

    try:
        response = ollama.generate(
            model=MODEL_NAME,
            prompt=prompt
        )

        parsed = extract_json(response.get("response", "")) or {}

        return {k: parsed.get(k, "Not specified") for k in FIELDS}

    except:
        return {k: "Error" for k in FIELDS}

# ---------------- MERGE ---------------- #

def merge_results(results: List[Dict]) -> Dict:
    combined = {k: [] for k in FIELDS}

    for r in results:
        if not isinstance(r, dict):
            continue

        for k in FIELDS:
            val = r.get(k)

            if not val or val in ["Not specified", "Error"]:
                continue
            if isinstance(val, dict):
                continue

            combined[k].append(val)

    final = {}

    for k, vals in combined.items():
        # ensure only hashable items
        safe_vals = [v for v in vals if isinstance(v, str)]

        unique = list(dict.fromkeys(safe_vals))

        final[k] = (
            " ".join(v.rstrip(".") + "." for v in unique)
            if unique else "Not specified"
        )

    return final

# ---------------- PIPELINE ---------------- #

def analyze_policy(text: str):

    sections = split_into_sections(text)
    st.write(f"📄 Detected {len(sections)} sections")

    section_summaries = []

    for i, (name, content) in enumerate(sections.items()):

        chunks = chunk_text(content, max_chars=3000, overlap=300)

        chunk_results = []

        for j, chunk in enumerate(chunks):
            with st.spinner(f"Section {i+1} chunk {j+1}/{len(chunks)}"):
                chunk_results.append(analyze_section(name, chunk))

        section_summaries.append(merge_results(chunk_results))


    return merge_results(section_summaries)



# ---------------- MAIN ---------------- #

def main():

    if "summary" not in st.session_state:
        st.session_state.summary = {}

    text = st.text_area("Paste Privacy Policy:", height=300)

    if st.button("Generate Summary"):
        if not text.strip():
            st.warning("Enter a privacy policy first.")
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