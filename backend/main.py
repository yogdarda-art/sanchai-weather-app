from dotenv import load_dotenv
load_dotenv()

import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import llm
from tools import get_weather

app = FastAPI()

# ✅ ONLY NEW PART (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    match = re.search(r"in\s+([a-zA-Z\s]+)", req.message.lower())
    city = match.group(1).strip() if match else req.message

    weather = get_weather(city)

    prompt = f"""
    User asked: {req.message}
    Weather data: {weather}

    Respond naturally using ONLY the weather data above.
    """

    reply = llm.invoke(prompt)
    return {"reply": reply.content}
