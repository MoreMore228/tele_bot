import telebot
import config
from p_dol import PrintDollar


rate_of_dollar_val = PrintDollar()


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.chat.type == 'Привет, бот!':
        welcome_sticker = open('stikers/welcome.webp', 'rb')
        bot.send_sticker(message.chat.id, welcome_sticker)
        bot.send_message(message.chat.id, "Привет, {0.first_name}".format(message.from_user))

        

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "/help - все команды бота\n/rateOFdollar - курс доллара")

@bot.message_handler(commands=['rateOFdollar'])
def rate_of_dollar(message):
    bot.send_message(message.chat.id, 'Курс - {0}'.format(rate_of_dollar_val))

bot.polling(none_stop=True)










