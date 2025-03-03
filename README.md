# Deepseek_TelegramBot
This bot helps you interact with DeepSeek in the Telegram environment. Similar to the experience of chatting with DeepSeek in a real conversation.


## How use it ? 
<ul>
<li><b>Create telegram bot</b></li> <br>
<p>Go to the @Bot_Father bot on Telegram, type the command <b>/newbot</b>, and provide the necessary information to create the Telegram bot. Then, copy the token and replace it with the value of the "TelegramBotToken" variable.</p>
<li><b>Getting the DeepSeek API</b></li> <br>
Go to the link https://platform.deepseek.com/api_keys, create an API token, copy the generated token, and replace it with the value of the "DeepseekApiToken" variable.
<li><b>Entering the bot usage (optional)</b></li> <br>
In step three, you need to provide a brief description of your requirements in the "BotEfficiency" variable. This will help DeepSeek's language model better understand your needs (optional).
<li><b>Forking the repository</b></li>
  
```git clone https://github.com/AmiraliTanabian/Deepseek_TelegramBot.git && cd Deepseek_TelegramBot```
<li><b>Installing the required packages</b></li><br>
```pip install telebot openai```
  <li><b>Run</b></li> <br>
  ```python3 main.py```
</ul>

## Explain for "stream=False"
If you've ever worked with language models (like ChatGPT or DeepSeek), you've probably noticed that when you make a request, the response appears gradually. This feature is quite appealing because it allows you to read the answer as it arrives, saving you time. However, this feature can sometimes lead to heavy processing, which may cause the bot to crash. Therefore, by default, it is set to False, but you can change it to True if you'd like.

## Error 402 : 
This error means that you do not have enough balance. To manage it, please visit the page: https://platform.deepseek.com/top_up.

You can view other errors through the following link:
https://api-docs.deepseek.com/quick_start/error_codes
