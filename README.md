# 🚀 CodeSight AI — Intelligent Code Understanding & Auto-Refactor Assistant

Video Demo: https://drive.google.com/drive/folders/1plooVAQ1bv1UU3ARa8eV3wdOEKqQv53o?usp=sharing
PPT File: https://drive.google.com/drive/folders/1plooVAQ1bv1UU3ARa8eV3wdOEKqQv53o?usp=sharing


CodeSight AI is an end-to-end **GenAI-powered developer assistant** that helps engineers understand, analyze, and automatically update large codebases.  
It combines **multi-agent architecture**, **impact analysis**, **automatic code fixing**, **GitHub import**, and a beautiful **Streamlit UI**.

This tool works with **ANY GitHub repository** (public or private) and supports **any programming language**.

---

## 🧠 Key Features

### 🔹 1. AI Chatbot (Gemini Powered)
Ask anything about your project, code logic, or architecture — chatbot answers instantly.

### 🔹 2. Smart Code Suggestions
Give natural language requests such as  
“Change login service to use OTP + JWT”  
and the agent returns real code snippets.

### 🔹 3. Code Generator
Generate new modules, controllers, services, utilities, or functions.

### 🔹 4. Repo Reader 📁  
Reads any folder or GitHub repo and gives:
- Full directory tree  
- Project summary  
- Files overview  
- Auto-detected tech stack  

### 🔹 5. Impact Analyzer 🔍  
Give a requirement → AI determines:
- Which files are affected  
- Impact level (High / Medium / Low)  
- Why they are impacted  
- Summary of required changes  

### 🔹 6. GitHub Importer 🌐  
Supports:
- Public repos  
- Private repos (token-based)  
- Auto-sync with Repo Reader and Impact Analyzer  

### 🔹 7. Auto Fixer 🪄  
AI automatically rewrites affected files based on your requirement:
- Reads the impacted files  
- Rewrites updated full code  
- Shows Before & After  
- Developer can download fixed files  

This makes CodeSight AI a real **developer co-pilot for entire projects**, not just single files.

---

## 📦 Tech Stack

- **Python 3.12**
- **Streamlit** (UI)
- **Gemini 2.5 Flash** (AI Model)
- **GitPython**
- **Multi-agent Architecture**
- **PowerShell + Git**
- Works on *any OS*: Windows, macOS, Linux

---

## 📂 Project Structure

codesight-ai/
│── app.py
│── agents/
│ ├── ai_core.py
│ ├── code_suggestions.py
│ ├── code_generator.py
│ ├── repo_reader.py
│ ├── impact_analyzer.py
│ ├── github_importer.py
│ ├── auto_fixer.py
│── demo_project/ # sample codebase for testing
│── .gitignore
│── requirements.txt
│── README.md
---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/manasapatil0608/codesight-ai.git
cd codesight-ai

2️⃣ Create a virtual environment
python -m venv .venv

3️⃣ Activate it
.venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Set your Gemini API key
setx GOOGLE_API_KEY "your-key-here"

6️⃣ Run the app
streamlit run app.py


