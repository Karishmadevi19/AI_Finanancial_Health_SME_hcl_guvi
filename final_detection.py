import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-flash-latest")


class FinalFinancialAdvisor:

    def __init__(self, data):
        self.data = data

    def get_advice(self, user_question):
        try:
            prompt = f"""
You are a professional CFO financial consultant.

Company recent financial data:
{self.data.tail(5)}

User Question:
{user_question}

Give highly specific financial advice.
Mention numbers, risk level, actions, and strategy.
"""

            response = model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"AI Error: {str(e)}"
