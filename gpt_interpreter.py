from dotenv import load_dotenv
import requests
import os

load_dotenv()

OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')
OPEN_AI_API_URL = os.environ.get('OPEN_AI_API_URL')

def send_api_request(user_input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post(OPEN_AI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception("ChatGPT API request failed.")


# Interpreter mode
#
# run: python gpt_interpreter.py
#
def main():
    try:
        while True:
            user_input = input("Query> ")
            print("\n" + "Query>\n", user_input)
            if user_input.lower() == "exit" or user_input.lower() == "stop":
                break
            print("\n" + "...waiting for api response..." + "\n")
            response = send_api_request(user_input)
            print("Response:\n\n", response + "\n")

    except KeyboardInterrupt:
        print("\nSaving session...\n\n[Process completed]\n")


if __name__ == "__main__":
    main()
