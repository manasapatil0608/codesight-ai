import os
import streamlit as st

from agents.parser import parse_requirement
from agents.search import search_files
from agents.scorer import score_file
from agents.reporter import generate_report


# ------------------------------------------
# Utility: Scan the demo_project folder
# ------------------------------------------
def scan_project(root="demo_project"):
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            file_paths.append(os.path.join(dirpath, f))
    return file_paths


# ------------------------------------------
# Streamlit UI
# ------------------------------------------
st.title("CodeSight AI — Intelligent Trace & Impact Explorer")

st.write(
    "Enter a requirement or change request. CodeSight AI will analyze the demo project "
    "and generate an Impact Map showing High/Medium/Low impact files with their scores."
)

requirement = st.text_area("Requirement or change description:", height=120)

if st.button("Analyze Impact"):
    if not requirement.strip():
        st.warning("Please enter a requirement before analyzing.")
    else:
        with st.spinner("Analyzing project..."):

            # 1. Scan project files
            files = scan_project()

            # 2. Parse requirement → keywords
            keywords = parse_requirement(requirement)

            # 3. Search candidate files
            candidates = search_files(keywords, files)

            if not candidates:
                st.error("No impacted files found for this requirement.")
            else:
                # 4. Score each candidate
                scored_files = {f: score_file(keywords, f) for f in candidates}

                # 5. Group into impact map
                impact_map = generate_report(scored_files)


        # ------------------------------------------
        # Show Results
        # ------------------------------------------
        if candidates:
            st.subheader("Detected Keywords")
            st.write(", ".join(keywords) if keywords else "None")

            st.subheader("Impact Map")

            for level in ["High", "Medium", "Low"]:
                items = impact_map[level]

                if not items:
                    continue

                if level == "High":
                    st.markdown("### 🔴 High Impact")
                elif level == "Medium":
                    st.markdown("### 🟡 Medium Impact")
                else:
                    st.markdown("### 🟢 Low Impact")

                for path, score in items:
                    st.markdown(f"- `{path}` — **Score:** {score}")
