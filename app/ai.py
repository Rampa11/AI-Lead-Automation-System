import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


def process_lead(message: str):
    try:
        if not client:
            return fallback_logic(message)

        prompt = f"""
        You are a sales assistant.

        Analyze this lead message:

        "{message}"

        Classify:
        - HOT = ready to buy / urgent / large quantity
        - WARM = interested but not urgent
        - COLD = low intent

        Return ONLY JSON:
        {{
            "status": "HOT/WARM/COLD",
            "summary": "short summary",
            "response": "professional reply"
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content

        print("AI RAW RESPONSE:", content)  # debug

        return json.loads(content)

    except Exception as e:
        print("AI ERROR:", e)
        return fallback_logic(message)


# ✅ CREATE IT HERE
def fallback_logic(message: str):
    message = message.lower()

    if any(word in message for word in ["buy", "purchase", "order", "units", "price", "urgent"]):
        return {
            "status": "HOT",
            "summary": "High intent buyer",
            "response": "Thanks for your interest. We’ll contact you immediately."
        }

    elif any(word in message for word in ["info", "details", "learn"]):
        return {
            "status": "WARM",
            "summary": "Needs more information",
            "response": "We’d be happy to share more details."
        }

    else:
        return {
            "status": "COLD",
            "summary": "Low intent",
            "response": "We’ll follow up later."
        }