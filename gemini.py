import google.generativeai as genai

api = "put_api"

genai.configure(api_key=api)

model = genai.GenerativeModel('gemini-pro')

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
