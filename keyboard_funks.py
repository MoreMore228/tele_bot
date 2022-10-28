from telebot import types



def keyboard_default():
    keyboard_default = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("/exchange")
    keyboard_default.add(btn1, btn2)
    return keyboard_default


def keyboard_start():
    keyboard_for_start = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    btn1 = types.KeyboardButton("Привет")
    btn2 = types.KeyboardButton("/help")
    btn3 = types.KeyboardButton("/exchange")
    keyboard_for_start.add(btn1, btn2, btn3)
    return keyboard_for_start


def keyboard_exchange():
    keyboard_for_rate = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    btn1 = types.KeyboardButton("/USD")
    btn2 = types.KeyboardButton("/EUR")
    btn3 = types.KeyboardButton("/CNY")
    btn4 = types.KeyboardButton("/GBP")
    btn5 = types.KeyboardButton("/help")
    keyboard_for_rate.add(btn1, btn2, btn3, btn4, btn5)
    return keyboard_for_rate


def after_rate():
    keyboard_after_rate = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    btn1 = types.KeyboardButton("Спасибо")
    btn2 = types.KeyboardButton("/exchange")
    btn3 = types.KeyboardButton("/help")
    keyboard_after_rate.add(btn1, btn2, btn3)
    return keyboard_after_rate