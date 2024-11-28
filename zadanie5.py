import telebot
import requests

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Команда /getemail, для отправки запроса.")

@bot.message_handler(commands=['getemail'])
def handle_getemail(message):
    response = requests.get('https://reqres.in/api/users/2')
    if response.status_code == 200:
        data = response.json()
        email = data['data']['email']
        bot.send_message(message.chat.id, f"Email пользователя: {email}")
    else:
        bot.send_message(message.chat.id, "Не удалось получить данные пользователя.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
