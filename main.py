import telebot
from telebot import types
TOKEN = '1656292393:AAHgABwHuEN32Iy6_zc7MtC1KOO7WcvsKes'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Дай файл')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Это тестовая версия бота оп обмену файлами...", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Дай файл':
        bot.send_message(message.chat.id, 'Да, секундочку...')
        doc = open('file.docx', 'rb')
        bot.send_document(message.chat.id, doc)
        bot.send_document(message.chat.id, "FILEID")

bot.polling()
