from openai import OpenAI
from prompts import SYSTEM_PROMPT
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_answer(query, web_context):
    response = client.chat.completions.create(
        model="mistralai/devstral-2512:free",  # FREE OpenRouter model
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Web Context:
{web_context}

Question:
{query}
"""
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
