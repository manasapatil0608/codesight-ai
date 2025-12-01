import os
from google import generativeai as genai

def load_project_files(root_path: str):
    """
    Returns [(filepath, filecontent)] for the entire project.
    """
    files = []
    for root, dirs, filenames in os.walk(root_path):
        for f in filenames:
            full = os.path.join(root, f)
            try:
                with open(full, "r", encoding="utf-8", errors="ignore") as file:
                    files.append((full, file.read()))
            except:
                continue
    return files


def analyze_impact(requirement: str, root_path: str):
    """
    Send requirement + project files to Gemini and get impact details.
    """

    project_files = load_project_files(root_path)
    files_summary = "\n".join([f"{i+1}. {path}" for i, (path, _) in enumerate(project_files)])

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    You are an expert software architect and impact analysis engineer.

    A new requirement/change request has been given:

    REQUIREMENT:
    {requirement}

    Below is the project file list:

    {files_summary}

    Your task:
    1. Identify which files will be impacted by this requirement.
    2. Classify each file as HIGH, MEDIUM, or LOW impact.
    3. Explain why each file is impacted.
    4. Show the exact code sections likely to change (just line numbers or functions).
    5. Suggest improvements and refactoring if needed.

    Return output in this format:

    HIGH IMPACT:
    - file1.js — reason, lines affected
    - file2.js — reason, lines affected

    MEDIUM IMPACT:
    - file3.js — reason

    LOW IMPACT:
    - file4.js — reason

    RECOMMENDATIONS:
    - …
    """

    response = model.generate_content(prompt)

    try:
        return response.text
    except:
        return "Error reading AI response."
