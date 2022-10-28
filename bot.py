import telebot
import config
import keyboard_funks as kb
from cur_pars import CurrencyParsing

# Список мата, для того, чтобы ругать людей :)
swearing = ['бля', 'блять', 'хуй', 'нахуй']

# Бот и его ТОКЕН
bot = telebot.TeleBot(config.TOKEN)


# ФУНКЦИЯ HELP
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "/help - все команды бота\n/exchange")


# ФУНКЦИЯ START
@bot.message_handler(commands=["start"])
def help(message):
    bot.send_message(message.chat.id, "Привет, я бот!\nЯ могу сказать тебе привет (команда: 'Привет')\nЯ могу подсказать все остальные команды (команда: /help)\nВыведу курс некоторых валют\nА еще могу отругать за 4 матерных слова!!!!", reply_markup=kb.keyboard_start())


# ФУНКЦИЯ КУРСА ВАЛЮТ
@bot.message_handler(commands=['exchange'])
def rate_of_dollar(message):
    bot.send_message(message.chat.id, 'Выберете курс, который хотите увидеть:\n/USD\n/EUR\n/CNY\n/GBP', reply_markup=kb.keyboard_exchange())
    

# для доллара 
@bot.message_handler(commands=['USD'])
def answer(message):
    bot.send_message(message.chat.id, 'Курс Доллара: {}'.format((CurrencyParsing('USD').get_val())), reply_markup=kb.after_rate())
    

# для евро
@bot.message_handler(commands=['EUR'])
def answer(message):
    bot.send_message(message.chat.id, 'Курс Евро: {}'.format((CurrencyParsing('EUR').get_val())), reply_markup=kb.after_rate())


# для юаня
@bot.message_handler(commands=['CNY'])
def answer(message):
    bot.send_message(message.chat.id, 'Курс Юаня: {}'.format((CurrencyParsing('CNY').get_val())), reply_markup=kb.after_rate())

# для стерлингов
@bot.message_handler(commands=['GBP'])
def answer(message):
    bot.send_message(message.chat.id, 'Курс Стерлингов: {}'.format((CurrencyParsing('GBP').get_val())), reply_markup=kb.after_rate())

# обработка текста
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'привет':
        welcome_sticker = open('stikers/welcome2.tgs', 'rb')
        bot.send_sticker(message.chat.id, welcome_sticker)
        bot.send_message(message.chat.id, "Привет, {0.first_name}".format(message.from_user))

    if message.text.lower() == "спасибо":
        pls_sticker = open("stikers/pls.webp", 'rb')
        bot.send_sticker(message.chat.id, pls_sticker)
        bot.send_message(message.chat.id, "Всегда пожалуйста, еба", reply_markup=kb.keyboard_default())
    if message.text.lower() in swearing:
        fuck_sticker = open("stikers/fuck.webp", 'rb')        
        bot.send_sticker(message.chat.id, fuck_sticker)
    
    else:
        None

bot.polling(none_stop=True, interval=0)



