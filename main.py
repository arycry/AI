from fastapi import FastAPI, Request
from chatbot import chat_with_groq

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Chatbot Perikanan aktif bro!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    response = chat_with_groq(prompt)
    return {"response": response}
