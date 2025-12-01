import streamlit as st
import os

from agents.ai_core import simple_chatbot
from agents.code_suggester import suggest_code_improvements
from agents.code_generator import generate_code_from_request
from agents.repo_reader import summarize_project
from agents.impact_analyzer import analyze_impact


# ======================================================
#  CUSTOM CSS (Purple Theme, Rounded UI, Modern Look)
# ======================================================
st.markdown("""
<style>

body {
    background-color: #F9F5FF;
}

/* ---- Gradient Title ---- */
h1.title-gradient {
    text-align: center;
    font-size: 48px;
    background: -webkit-linear-gradient(#7B2FF7, #C084FC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ---- Buttons ---- */
.stButton>button {
    background: linear-gradient(135deg, #7B2FF7, #9F6BFF);
    color: white !important;
    border-radius: 10px;
    padding: 10px 25px;
    border: none;
    font-size: 16px;
}
.stButton>button:hover {
    background: linear-gradient(135deg, #9F6BFF, #7B2FF7);
    cursor: pointer;
}

/* ---- Input Fields ---- */
.stTextInput>div>div>input,
.stTextArea textarea {
    border-radius: 10px !important;
    border: 2px solid #C084FC !important;
}

/* ---- Card Container ---- */
.card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 4px 15px rgba(123, 47, 247, 0.08);
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# ======================================================
#  SIDEBAR (Branding)
# ======================================================
with st.sidebar:
    st.markdown("""
        <h1 style='color:#7B2FF7;'>CodeSight AI</h1>
        <p>Your AI-powered assistant for code analysis and generation.</p>
        <hr>
        <h3>📌 Features</h3>
        <ul>
            <li>Chatbot</li>
            <li>Code Suggestions</li>
            <li>Code Generator</li>
            <li>Repo Reader</li>
            <li>Impact Analyzer</li>
            <li>Import from Github</li>
            <li>Auto Fixer</li>
                
        </ul>
        <hr>
        <p style='font-size:13px; color:gray;'>Version 1.0 • Built by Manasa 💜</p>
    """, unsafe_allow_html=True)


# ======================================================
#  TITLE
# ======================================================
st.markdown("<h1 class='title-gradient'>CodeSight AI</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#555; font-size:20px;'>AI Developer Tool for Code Understanding, Debugging & Automation</p>",
    unsafe_allow_html=True
)
st.write("")

# -------------------------------
# Session state for GitHub repo sync
# -------------------------------
if "imported_repo_path" not in st.session_state:
    st.session_state.imported_repo_path = None

# ======================================================
#  TABS
# ======================================================
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "💬 Chatbot",
    "🛠 Code Suggestions",
    "✨ Code Generator",
    "📁 Repo Reader",
    "📊 Impact Analyzer",
    "🌐 GitHub Import",
    "🪄 Auto Fixer"
])

# ======================================================
#  TAB 1 — CHATBOT
# ======================================================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("💬 Chatbot – Ask Anything")

    user_input = st.text_input("Your message:")

    if st.button("Send", key="chat_button"):
        if user_input.strip():
            with st.spinner("Thinking..."):
                reply = simple_chatbot(user_input)
            st.markdown("### 🟣 Response:")
            st.write(reply)
        else:
            st.warning("Please type something.")

    st.markdown("</div>", unsafe_allow_html=True)


# ======================================================
#  TAB 2 — CODE SUGGESTIONS
# ======================================================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🛠 Improve Your Code")

    code_text = st.text_area(
        "Paste your code here:",
        height=250,
        placeholder="Example: def login_user(username, password): ..."
    )

    if st.button("Analyze Code", key="suggest_button"):
        if code_text.strip():
            with st.spinner("Analyzing your code..."):
                result = suggest_code_improvements(code_text)
            st.markdown("### 🟣 Suggestions:")
            st.write(result)
        else:
            st.warning("Please paste some code.")

    st.markdown("</div>", unsafe_allow_html=True)


# ======================================================
#  TAB 3 — CODE GENERATOR
# ======================================================
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("✨ Generate Code from English")

    request = st.text_area(
        "Describe what code to generate:",
        height=200,
        placeholder="Example: Generate authentication code using JWT"
    )

    if st.button("Generate Code", key="generate_button"):
        if request.strip():
            with st.spinner("Generating code..."):
                result = generate_code_from_request(request)
            st.markdown("### 🟣 Generated Code:")
            st.code(result)
        else:
            st.warning("Please enter a description.")

    st.markdown("</div>", unsafe_allow_html=True)


# ======================================================
#  TAB 4 — REPO READER
# ======================================================
with tab4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📁 Project Structure & Summary")

    default_repo = st.session_state.imported_repo_path or "demo_project"

    folder_path = st.text_input(
        "Project folder path:",
        value=default_repo,
        key="repo_reader_path"
    )

    if st.session_state.imported_repo_path:
        st.success(f"Connected to imported repo: {st.session_state.imported_repo_path}")

    if st.button("Scan Project", key="repo_button"):
        if os.path.exists(folder_path):
            with st.spinner("Reading and summarizing project..."):
                result = summarize_project(folder_path)
            st.markdown("### 🟣 Project Summary:")
            st.write(result)
        else:
            st.error("Folder not found!")

    st.markdown("</div>", unsafe_allow_html=True)


# ======================================================
#  TAB 5 — IMPACT ANALYZER
# ======================================================

with tab5:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📊 Impact Analyzer — Find Which Files Will Be Affected")

    # Use imported GitHub repo if available
    default_repo = st.session_state.imported_repo_path or "demo_project"

    folder = st.text_input(
        "Project folder:",
        value=default_repo,
        key="impact_analyzer_path"
    )

    if st.session_state.imported_repo_path:
        st.success(f"Using imported repo: {st.session_state.imported_repo_path}")

    requirement = st.text_area(
        "Describe the requirement/change:",
        height=150,
        placeholder="Example: Change authentication to JWT with email OTP"
    )

    if st.button("Analyze Impact", key="impact_button"):
        if requirement.strip():
            with st.spinner("Analyzing impact..."):
                result = analyze_impact(requirement, folder)

            st.markdown("### 🟣 Impact Report:")
            st.write(result)
        else:
            st.warning("Please describe the requirement first.")

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 6 — IMPORT FROM GITHUB
# ----------------------------------------------------
with tab6:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🌐 Import Project from GitHub")

    github_url = st.text_input(
        "Enter GitHub repository URL:",
        placeholder="Example: https://github.com/user/repo"
    )

    import_type = st.radio("Repository Type:", ["Public Repo", "Private Repo"])

    if import_type == "Private Repo":
        token = st.text_input("Enter Personal Access Token:", type="password")
    else:
        token = None

    if st.button("Import Repository"):
        if github_url.strip():
            from agents.github_importer import clone_public_repo, clone_private_repo

            with st.spinner("Importing repository..."):
                if import_type == "Public Repo":
                    result = clone_public_repo(github_url)
                else:
                    result = clone_private_repo(github_url, token)

            st.markdown("### 🟣 Import Result:")
            st.write(result)
        else:
            st.warning("Please enter a GitHub repo URL.")

    st.markdown("</div>", unsafe_allow_html=True)
# ----------------------------------------------------
# TAB 7 — AUTO FIXER (AI Rewrite Impacted Files)
# ----------------------------------------------------
with tab7:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🪄 Auto Fixer — AI Updates Your Code Automatically")

    requirement = st.text_area(
        "Describe the change request:",
        height=160,
        placeholder="Example: Change authentication to JWT and add OTP verification."
    )

    default_repo = st.session_state.imported_repo_path or "demo_project"
    folder = st.text_input(
        "Project folder:",
        value=default_repo,
        key="auto_fixer_repo_path"
    )

    if st.button("Find Impacted Files", key="auto_fixer_find"):
        from agents.impact_analyzer import analyze_impact
        with st.spinner("Identifying impacted files..."):
            impact_text = analyze_impact(requirement, folder)

        st.session_state.impact_result_text = impact_text
        st.markdown("### 🔍 Impact Analysis Result:")
        st.write(impact_text)

        # Extract file paths (simple approach)
        impacted_files = []
        for line in impact_text.splitlines():
            if "-" in line and "." in line:  # e.g. "- auth/login.py"
                filepath = line.split("–")[0].strip().replace("-", "").strip()
                if os.path.exists(filepath):
                    impacted_files.append(filepath)

        st.session_state.impacted_files = impacted_files

        if impacted_files:
            st.success("Impacted files found!")
        else:
            st.error("Could not detect file paths automatically.")

    if st.button("Apply Auto Fix", key="auto_fixer_apply"):
        if "impacted_files" not in st.session_state or not st.session_state.impacted_files:
            st.error("Please run Impact Finder first.")
        else:
            from agents.auto_fixer import apply_auto_fix

            with st.spinner("Applying fixes..."):
                results = apply_auto_fix(requirement, st.session_state.impacted_files)

            st.markdown("### 🪄 Updated Files")

            for file, content in results.items():
                st.markdown(f"#### 📄 {file}")
                st.markdown("**Before:**")
                st.code(content["before"])
                st.markdown("**After:**")
                st.code(content["after"])

    st.markdown("</div>", unsafe_allow_html=True)
