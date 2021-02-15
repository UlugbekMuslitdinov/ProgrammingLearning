from typing import Text
import telebot 
import urllib

token = '1586246356:AAEAwFmyu4PckC-RmlmNVGre-JVXpvVCzHk'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handler_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('photo', 'audio', 'docs')
    user_markup.row('sticker', 'video', 'voice', 'location')
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handler_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'sticker':
        bot.send_sticker(message.from_user.id, con)
        


bot.polling(none_stop=True)