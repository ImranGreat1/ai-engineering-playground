from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

def chat_with_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def chat_with_ruby(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a cat. Your name is Ruby"
        ),
        contents=prompt
    )

    return response.text


def stream_chat_with_gemini(prompt):
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    for chunk in stream:
        yield chunk.text


def chat_with_a_cat_stream(prompt):
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="You are a cat. Your name is Ruby"
        ),
        contents=prompt
    )

    for chunk in stream:
        yield chunk.text


def discuss_with_gemini(prompt, prevChat):
    if not prevChat:
        chat = client.chats.create(model="gemini-2.5-flash-lite")
    else:
        chat = prevChat

    response = chat.send_message(prompt)
    return { "text": response.text, "chat": chat }


def discuss_with_gemini_stream(prompt, prevChat):
    if not prevChat:
        chat = client.chats.create(model="gemini-2.5-flash-lite")
    else:
        chat = prevChat

    response = chat.send_message_stream(prompt)

    for chunk in response:
        yield { "text": chunk.text, "chat": chat }
    
