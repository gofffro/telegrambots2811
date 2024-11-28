import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
     bot.send_message(message.chat.id, 'Я отвечаю, только на голосовые сообщения:')

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.reply_to(message, "Услышал тебя родной")

if __name__ == '__main__':
    bot.polling(none_stop=True)
