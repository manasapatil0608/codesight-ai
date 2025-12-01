import os
import google.generativeai as genai

print("google-generativeai version:", genai.__version__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    models = list(genai.list_models())
    print("Models available:")
    for m in models:
        print(" -", m.name)
except Exception as e:
    print("Error while listing models:")
    print(repr(e))
