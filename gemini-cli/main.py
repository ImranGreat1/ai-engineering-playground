from services.gemini import discuss_with_gemini_stream


print("Chat with Gemini LLM in the command line...")


# while True:
#     prompt = input("You: ")
#     if prompt.lower() == "exit":
#         break

#     response = chat_with_gemini(prompt=prompt)
#     print(f'gemini: {response}')


# while True:
#     print("")
#     prompt = input("You: ")
#     if prompt.lower() == "exit":
#         break

#     response = stream_chat_with_gemini(prompt=prompt)
#     print(f"gemini: ", end="")
#     for chunk_text in response:
#         print(chunk_text, end="")


# while True:
#     print("")
#     prompt = input("You: ")
#     if prompt.lower() == "exit":
#         break

#     response = chat_with_a_cat(prompt=prompt)
#     print(f"gemini: ", end="")
#     for chunk_text in response:
#         print(chunk_text, end="")

# chat = None
# while True:
#     print("")
#     prompt = input("You: ")
#     if prompt.lower() == "exit":
#         break

#     response = discuss_with_gemini(prompt=prompt, prevChat=chat)
#     chat = response["chat"]
#     print(f"gemini: ", end="")
#     print(response["text"])


chat = None
while True:
    print("")
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    response = discuss_with_gemini_stream(prompt=prompt, prevChat=chat)
    print(f"gemini: ", end="")
    for chunk in response:
        print(chunk["text"], end="")
        chat = chunk["chat"]