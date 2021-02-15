import telebot 


token = '1586246356:AAEAwFmyu4PckC-RmlmNVGre-JVXpvVCzHk'
bot = telebot.TeleBot(token)

print(bot.get_me())

def log(message, answer):
    print("\n =====")
    from datetime import datetime
    print(datetime.now())
    print("Message from (0) (1) . (id = (2)) \n Text - (3)".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    print(answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Oh, I can help you')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "You can't play it"
    if message.text == 'a':
        answer = "B"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
        
    elif message.text == 'b':
        answer = "hi"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    else:
        bot.send_message(message.chat.id, "Oh, you're wrong")
        log(message, answer)



bot.polling(none_stop=True, interval=0)