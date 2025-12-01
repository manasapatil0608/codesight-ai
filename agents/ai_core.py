import os
import google.generativeai as genai

# Configure the API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def simple_chatbot(question: str) -> str:
    """
    Sends a message to Gemini and returns the chatbot response.
    Uses gemini-2.5-flash (the model verified to work on your account).
    """
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")  # IMPORTANT!
        response = model.generate_content(question)

        # Some responses return .text, some return candidates
        if hasattr(response, "text"):
            return response.text

        # Fallback for candidate-based structure
        return "\n".join(
            part.text 
            for part in response.candidates[0].content.parts
            if hasattr(part, "text")
        )

    except Exception as e:
        return f"❌ ERROR from Gemini:\n{str(e)}"
