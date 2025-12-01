import os
from google import generativeai as genai

def read_project_files(root_path: str):
    """
    Walk through project folder and load all file paths + content.
    Returns a list of (path, content).
    """
    collected = []

    for root, dirs, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(root, file)

            # Only read text/code files
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                collected.append((full_path, content))
            except:
                continue

    return collected


def summarize_project(root_path: str):
    """
    Summarizes the entire project using Gemini.
    """
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        files = read_project_files(root_path)
        file_list_text = "\n".join([f"{i+1}. {x[0]}" for i, x in enumerate(files)])

        prompt = f"""
        You are an expert software architect.
        Analyze the following project structure and generate a detailed summary.

        PROJECT FILES:
        {file_list_text}

        For each file, provide:
        - What it does
        - Key functions
        - Purpose in the system
        - How it connects to other files
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error summarizing project: {e}"
