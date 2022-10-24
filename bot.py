import telebot
import config
from p_dol import PrintDollar

swearing = ['бля', 'блять', 'хуй', 'нахуй']
rate_of_dollar_val = PrintDollar()


bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "/help - все команды бота\n/rateOFdollar - курс доллара")

@bot.message_handler(commands=['rateOFdollar'])
def rate_of_dollar(message):
    bot.send_message(message.chat.id, 'Курс - {0}'.format(rate_of_dollar_val))

@bot.message_handler(content_types = ['text'])
def answer(message):
    if message.text.lower() == 'привет':
        welcome_sticker = open('stikers/welcome2.tgs', 'rb')
        bot.send_sticker(message.chat.id, welcome_sticker)
        bot.send_message(message.chat.id, "Привет, {0.first_name}".format(message.from_user))

    if message.text.lower() in swearing:
        bot.send_message(message.chat.id, 'Вая, не ругайся!!!')
    
    else:
        # bot.send_message(message.chat.id, 'Не знаю что сказать :(')
        None

bot.polling(none_stop=True, interval=0)



