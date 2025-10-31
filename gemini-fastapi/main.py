from fastapi import FastAPI
from pydantic import BaseModel
from services.gemini import chat_with_gemini, chat_with_ruby, chat_with_a_cat_stream

class Prompt(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask_gemini(prompt: Prompt):
    return chat_with_gemini(prompt=prompt.text)


@app.post("/ask-a-cat")
def ask_cat(prompt: Prompt):
    return chat_with_ruby(prompt=prompt)