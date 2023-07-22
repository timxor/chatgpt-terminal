# chatgpt-terminal

chatgpt-terminal

## 1. Download required libraries

```
pip install -r requirements.txt
```


## 2. Add OpenAI API key

Generate and copy a new OpenAI API key from API Key settings website: 
https://platform.openai.com/account/api-keys

Put your new api key in a new file called ```.env```.

```
touch .env
nano .env
OPEN_AI_API_KEY=your-openai-api-key-goes-here
```


## 3. Copy files & add alias

Copy gpt.py:
```
chmod +x gpt_cli.py
sudo cp gpt_cli.py /usr/local/bin/gpt_cli.py

chmod +x .env
sudo cp .env /usr/local/bin/.env
```

Add alias:
``` 
nano ~/.zshrc
alias gpt="python gpt_cli.py"
source ~/.zshrc
```

## 4. Run gpt_cli.py

Run with alias:
``` 
gpt hello there, how are you?
```

Run without alias:
``` 
python gpt_cli.py hello there, how are you?
```

## 5. Run gpt_interpreter.py

Run without alias:
``` 
python gpt_interpreter.py
```

Run with alias:
``` 
gpt_interpreter
```

