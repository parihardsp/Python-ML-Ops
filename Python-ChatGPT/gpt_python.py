from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY")
)

messages = [
    {"role": "system",
     "content": "You are a very witty and funny assistant. You always try to add humor in all your answers. You also use emojis etc."},
    {"role": "user", "content": "Do you know where I can find the best mountains in the world?"},
    {"role": "assistant",
     "content": "Hmmm! Adventurous guy. I guess you like heights. So the best mountains you can find are in the Himalayas of India and Switzerland."},
    {"role": "user", "content": "Where can I find the best food in the world? List 3 countries. Answer in line wise"},
]

# prompt = "What's the most popular ski resort in Europe?"

chat_completion = client.chat.completions.create(
    messages=messages,
    model="gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)
