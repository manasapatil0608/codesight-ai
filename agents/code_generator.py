from google import generativeai as genai
import os

def generate_code_from_request(request: str) -> str:
    """
    Convert natural language instructions into ready-to-use code.
    """
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        prompt = f"""
        You are a senior full-stack engineer.
        Convert the following natural-language request into HIGH-QUALITY CODE.

        - Write clean, production-ready code
        - Include comments
        - If the user asks for changes, generate the updated file or function
        - If needed, explain how to integrate the code

        Request:
        {request}

        Return ONLY code unless explanation is required.
        """

        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text

        return "\n".join(
            part.text for part in response.candidates[0].content.parts if hasattr(part, "text")
        )

    except Exception as e:
        return f"Error in code generation: {e}"
