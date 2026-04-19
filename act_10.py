from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

MODEL_NAME = "google/gemma-4-4b"

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("💬 Chatbot started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages
    )

    reply = response.choices[0].message.content

    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})