from google import generativeai as genai
import os

def suggest_code_improvements(code_snippet: str) -> str:
    """
    Sends code to Gemini and receives improvement suggestions.
    """
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash")  # working model

        prompt = f"""
        You are a senior software engineer and code reviewer.
        Analyze the following code and provide:

        1. Bugs or errors
        2. Performance improvements
        3. Cleaner / optimized version of the code
        4. Best practices that should be followed
        5. Security concerns (if any)

        Code:
        ```
        {code_snippet}
        ```

        Provide the response in clear bullet points.
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error in code suggestions: {e}"
