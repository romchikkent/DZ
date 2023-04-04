# 5969930057:AAF10Sspyp-eTPqDMMAOeZiKTVfmr-lsI5M
import telebot
from telebot import types

token = '5969930057:AAF10Sspyp-eTPqDMMAOeZiKTVfmr-lsI5M'
bot = telebot.TeleBot(token)


def virtual_klava():
    klava = types.InlineKeyboardMarkup()
    privetstvie = types.InlineKeyboardButton(text='Привет бот', callback_data='1')
    proshanie = types.InlineKeyboardButton(text='Пока бот', callback_data='2')
    anecdot = types.InlineKeyboardButton(text='Хочу анекдот', callback_data='3')
    spati = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')

    klava.add(privetstvie, proshanie, anecdot, spati)
    return klava


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Привет',
                     reply_markup=virtual_klava())


@bot.callback_query_handler(func=lambda call: True)
def collback_inline(call):
    if call.message:
        if call.data == '1':
            txt = 'Здравствуйте'
            bot.send_message(chat_id=call.message.chat.id, text=txt, reply_markup=virtual_klava())
        if call.data == '2':
            txt = 'Досвидание'
            bot.send_message(chat_id=call.message.chat.id, text=txt, reply_markup=virtual_klava())
        if call.data == '3':
            txt = '– Какая должна быть женщина? - Как поликлиника – чистой, общедоступной и бесплатной.'
            bot.send_message(chat_id=call.message.chat.id, text=txt, reply_markup=virtual_klava())
        if call.data == '4':
            txt = 'Сладких снов'
            bot.send_message(chat_id=call.message.chat.id, text=txt, reply_markup=virtual_klava())


bot.polling(none_stop=True)
