# chatgpt-terminal

chatgpt-terminal

## 1. Download required libraries

```
pip install -r requirements.txt

```


## 2. Add OpenAI API key

Generate and copy a new OpenAI API key from API Key settings website: https://platform.openai.com/account/api-keys

Put your new api key in a new file called ```.env```.

```
touch .env

nano .env

OPEN_AI_API_KEY=your-openai-api-key-goes-here
```


## 3. Copy files & add alias

Copy gpt.py:
```
chmod +x gpt.py
sudo cp gpt.py /usr/local/bin/gpt.py

chmod +x .env
sudo cp .env /usr/local/bin/.env
```

Add alias:
``` 
nano ~/.zshrc
alias gpt="python gpt.py"
source ~/.zshrc
```

## 4. Run 





