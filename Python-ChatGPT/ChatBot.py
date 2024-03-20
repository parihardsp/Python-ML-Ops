from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY")
)


def chat_with_gpt(prompt):
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system", "content": "You are a helpful assistant. You give witty replies with emojis"},{ "role": "user", "content": prompt}]
    )

    return chat.choices[0].message.content.strip()


'''
OpenAI.chat.completions.create(
    model="",
    messages=[]
)
'''

print(__name__)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye", "quit"]:
            print('Chatbot: Thanks for chatting!')
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
