from operator import le
import telebot
from telebot import types
import json
import main


TOKEN = '5558614303:AAGkXh0MT06VJg-fibA4BXLt90D8sknzBC8'

bot = telebot.TeleBot(TOKEN)

cars = []

with open('machine-kg/pars.json', 'r', encoding="utf-8-sig") as file:
    cars = json.load(file)


@bot.message_handler(commands=['start'])
def message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Выбрать марку машины")
    markup.add(item)

    #bot.send_message(message.chat.id) #через сообщение обратились к чату и получили его id
    bot.send_message(message.chat.id, "Привет, <b>{0.first_name}</b>".format(message.from_user, bot.get_me()),
    parse_mode = 'html', reply_markup = markup)


@bot.message_handler()
def get_user_text(message):
    match message.text:
        case "Выбрать марку машины":
            markup = types.InlineKeyboardMarkup(row_width=2 )
            for car in cars:
                markup.add(types.InlineKeyboardButton(car, callback_data=f"select_car/{car}/{message.chat.id}"),row_width=2)
            bot.send_message(message.chat.id, '<u><b>Выберите марку машины</b></u>', reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    match call.data.split('/'):
        case 'select_car', car_name, id:
            markup = types.InlineKeyboardMarkup(row_width=2)
            for i in range(len(cars[car_name])):
                markup.add(types.InlineKeyboardButton(f'{cars[car_name][i]["cars_name"]}-{cars[car_name][i]["year"]}', callback_data=f"select_mark/{car_name}/{i}/{id}"),row_width=2)

            bot.send_message(id, '<u><b>Выберите модель машины</b></u>', reply_markup=markup, parse_mode='html')
        case 'select_mark', car_name, car_mark, id:
            bot.send_message(id, cars[car_name][int(car_mark)]["href"], parse_mode = 'html')
        case _:
            print("Error")

bot.polling(none_stop = True) #бот работает без остановки 

