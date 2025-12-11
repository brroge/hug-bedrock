import requests
import os

API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def ask_huggingface(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

if __name__ == "__main__":
    print("Chatbot is ready!")
    reply = ask_huggingface("Hello, how are you?")
    print("Sample reply:", reply)
