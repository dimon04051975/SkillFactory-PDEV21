import telebot
import requests
import json
#import Exception

#class MyException(Exception):
    #pass

#class ConverterValyut:
    #@staticmethod
    #def convert(self, message: telebot.types.Message):
        #values = message.text.split(' ')

        #if len(values) != 3:
            #raise MyException('Неверное количество параметров.')

        #quote, base, amount = values

token = "5857895457:AAGS5Lb-xj-Zm-nTcRC73NJhAa-Ue_29-7g"

bot = telebot.TeleBot(token)

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'биткоин': 'BTC',
    'рубль': 'RUR',
}

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Введите команду боту в формате:\n<имя валюты> \
    <в какую валюту перевести> \
    <колличество валюты>\n Увидеть список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    p = float(amount)
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')

    total_base = json.loads(r.content)[keys[base]]
    s = float(total_base)
    sum_valyta = p*s
    text = f'Цена {amount} {quote} в {base} - {sum_valyta}'
    bot.send_message(message.chat.id, text)



bot.polling()