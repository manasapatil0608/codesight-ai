import os
from google import generativeai as genai

def apply_auto_fix(requirement: str, impacted_files: list):
    """
    AI automatically updates impacted files based on requirement.
    Returns a dictionary of:
    {
      "filename": {
        "before": "...",
        "after": "..."
      }
    }
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    results = {}

    for filepath in impacted_files:
        try:
            # Read original file
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                original_code = f.read()

            prompt = f"""
            You are a senior software engineer.

            A new change request has been given:

            REQUIREMENT:
            {requirement}

            Below is the current file content. Update this file based on the requirement.
            - Follow best practices
            - Keep same language/framework
            - Do not remove unrelated code
            - Return ONLY the updated full code file

            CURRENT FILE: {filepath}

            CODE:
            {original_code}
            """

            response = model.generate_content(prompt)

            updated_code = response.text if hasattr(response, "text") else ""

            results[filepath] = {
                "before": original_code,
                "after": updated_code
            }

        except Exception as e:
            results[filepath] = {
                "before": "",
                "after": f"Error processing file: {e}"
            }

    return results
