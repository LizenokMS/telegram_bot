import telebot
from telebot import types
import random

bot = telebot.TeleBot("6777926019:AAHUMROf4Zk80g0TDYvU-8bcilqD_FHWH2U")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Рандомное число"))
    markup.add(types.KeyboardButton("Рандомный напиток"))
    markup.add(types.KeyboardButton("Рандомный стикер"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(content_types=['text'])
def randomize(message):
    if message.text == 'Рандомное число':
        num = random.randint(1, 100)
        bot.send_message(message.chat.id, str(num))
    if message.text == 'Рандомный напиток':
        a = ['Сок', 'Чай','Кисель', 'Газировка', 'Кофе']
        bot.send_message(message.chat.id, random.choice(a))
    if message.text == 'Рандомный стикер':
        link = ['sticker/0.webp', 'sticker/1.webp', 'sticker/2.webp', 'sticker/3.webp', 'sticker/4.webp', 'sticker/5.webp', 'sticker/6.webp', 'sticker/7.webp', 'sticker/8.webp']
        bot.send_sticker(message.chat.id, open(random.choice(link), 'rb'))

bot.polling(none_stop=True)
