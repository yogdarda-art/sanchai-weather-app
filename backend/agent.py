from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="allenai/olmo-3.1-32b-think:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Sanchai Weather App",
    },
)
