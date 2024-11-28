import telebot
from telebot import types

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выберите номер:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text.lower() == "закрыть":
        bot.send_message(message.chat.id, "Клавиатура удалена", reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}")

if __name__ == '__main__':
    bot.polling(none_stop=True) 
