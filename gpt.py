from openai import OpenAI
import os

Key2 = os.getenv("key1")
client = OpenAI(api_key = Key2,base_url="https://api.chatanywhere.tech/v1")

def gpt_35_api(messages:list):
    completion = client.chat.completions.create(model = "gpt-3.5-turbo",messages = messages)
    return completion.choices[0].message.content   

