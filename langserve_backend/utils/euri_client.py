import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EURI_API_KEY')
BASE_URL = "https://api.euron.one/api/v1/euri"

def chat_completion(messagges, model="gpt-4.1-nano", temperature=0.7, max_tokens=1000):
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "messages": messagges,
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']