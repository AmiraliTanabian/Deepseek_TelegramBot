from openai import OpenAI
from telebot import TeleBot

DeepseekApiToken = '<YOUR_DEEPSEEK_API_TOKEN>' # Get from --> https://platform.deepseek.com/api_keys
TelegramBotToken = '<YOUR_Telegram_API_TOKEN>' # Get from @Bot_Father on telegram
BotEfficiency = '<The_Expectation_You_Have_From_The_Bot>' # Helps improve the performance of DeepSeek's language model.

bot = TeleBot(TelegramBotToken)
client_side = OpenAI(api_key=DeepseekApiToken, base_url='https://api.deepseek.com')

@bot.message_handler(content_types=['text'])
def main(msg):
    try:
        result = client_side.chat.completions.create(
        model = 'deepseek-chat',
        messages = [
            {'role':'system', 'content':BotEfficiency},
            {'role':'user' , 'content':msg.text}
        ],
        stream=False
        )

        bot.send_message(msg.chat.id, result.choices[0].message.content)
    except Exception as Error :
        print(f"Error : {Error}")
        bot.send_message(msg.chat.id, 'Error! Please try agian')

@bot.message_handler(content_types=['video', 'photo', 'audio'])
def another_types(msg):
    bot.send_message(msg.chat.id, 'Please send text message!')

bot.polling(timeout=60, non_stop=True)
