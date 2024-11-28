import telebot
from telebot import types

TOKEN = ''

LINKS = {
    'Тестирование': [
        ('QAStack', 'https://qastack.ru', 'Сообщество тестировщиков ПО'),
        ('Habr QA', 'https://habr.com/ru/hub/qa/', 'Статьи и новости о тестировании'),
    ],
    'Разработка': [
        ('Habr', 'https://habr.com', 'Платформа для разработчиков и IT-специалистов'),
        ('Stack Overflow', 'https://stackoverflow.com', 'Сайт вопросов и ответов для программистов'),
    ],
    'Образование': [
        ('Coursera', 'https://www.coursera.org', 'Онлайн-курсы от ведущих университетов и компаний'),
        ('Udemy', 'https://www.udemy.com', 'Онлайн-курсы по различным темам'),
    ]
}

bot = telebot.TeleBot(TOKEN)

def createMainMenu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Тестирование", callback_data='Тестирование'))
    markup.add(types.InlineKeyboardButton("Разработка", callback_data='Разработка'))
    markup.add(types.InlineKeyboardButton("Образование", callback_data='Образование'))
    return markup

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = createMainMenu()
    bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
    if call.data == 'Назад':
        markup = createMainMenu()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите категорию:', reply_markup=markup)
    else:
        category = call.data
        links = LINKS.get(category, [])
        message = f"Ссылки по категории {category}:\n\n"
        for name, url, description in links:
            message += f"[{name}]({url}) - {description}\n"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Назад", callback_data='Назад'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup=markup, parse_mode='Markdown')

if __name__ == '__main__':
    bot.polling(none_stop=True)
