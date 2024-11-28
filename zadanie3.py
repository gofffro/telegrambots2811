import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, как тебя зовут?")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_input = message.text.lower()
    
    if "зовут" in user_input:
        bot.send_message(message.chat.id, f"Тебя зовут {user_input.split()[-1]}, сколько тебе лет?")
    elif "лет" in user_input:
        bot.send_message(message.chat.id, f"Тебе {user_input.split()[0]}, где ты живешь?")
    elif "живу" in user_input:
        bot.send_message(message.chat.id, f"Ты живешь в {user_input.split()[-1]}, чем занимаешься?")
    else:
        bot.send_message(message.chat.id, f"'{user_input}', интересно, расскажи еще что-нибудь.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
