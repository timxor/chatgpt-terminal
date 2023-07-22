from dotenv import load_dotenv
import requests
import sys
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


# CLI / terminal pass arguments mode
#
# run: python gpt_cli.py your_message
#
def main():
    new_argument = ""
    if len(sys.argv) > 1:
        argument = " ".join(sys.argv[1:])
        new_argument = "'" + argument + "'"
    else:
        print("No argument provided.")
        sys.exit(1)

    user_input = new_argument
    print("\n" + "Query:\n\n", user_input)

    print("\n" + "...waiting for api response..." + "\n")

    response = send_api_request(user_input)
    print("Response:\n\n", response + "\n")


if __name__ == "__main__":
    main()
