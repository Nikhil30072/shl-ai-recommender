from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from recommender import search_assessments

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):

    latest_message = req.messages[-1].content

    if len(latest_message.split()) < 3:
        return {
            "reply": "Please provide more details about the role.",
            "recommendations": [],
            "end_of_conversation": False
        }

    results = search_assessments(latest_message)

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"]
        })

    return {
        "reply": "Here are recommended SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }