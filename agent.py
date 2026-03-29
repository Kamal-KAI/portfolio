import os
from openai import OpenAI
from llm_context import PROFILE_CONTEXT, PAGE_CONTEXT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are Kamal Kishor's portfolio assistant.

Your job:
- Answer questions about Kamal's profile, experience, projects, and interests
- Summarize the current page when asked
- Stay grounded only in the provided context
- Do not invent facts not present in the provided context
- Be concise, warm, and professional
"""

def get_portfolio_response(user_query: str, current_page: str, page_data: str = "") -> str:
    page_context = PAGE_CONTEXT.get(current_page.lower(), "")

    prompt = f"""
Global Profile Context:
{PROFILE_CONTEXT}

Current Page Context:
{page_context}

Structured Page Data:
{page_data}

User Question:
{user_query}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content