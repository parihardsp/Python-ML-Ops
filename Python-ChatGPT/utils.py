from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY")
)


def generate_description(input):
    message = [{"role": "system",
                "content": """As a Product Description Generator, Generate a multi paragraph rich text product description 
               with emojis from information provided to you \n"""},
               {"role": "user", "content": f"{input}"}]

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    reply = chat_completion.choices[0].message.content
    return reply
