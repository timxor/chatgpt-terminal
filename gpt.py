from dotenv import load_dotenv
import requests
import sys
import os

load_dotenv()

OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')
OPEN_AI_API_URL = os.environ.get('OPEN_AI_API_URL')

def chat_with_gpt3(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(OPEN_AI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception("ChatGPT API request failed.")

def main():
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_gpt3(user_input)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()
