import telebot
from telebot import types
import os
from flask import Flask , request



tokenn = "5372408948:AAGHqBkVbHjKzz7DuGZ8QMWzSd9EbtUT01Q"
bot = telebot.TeleBot("5372408948:AAGHqBkVbHjKzz7DuGZ8QMWzSd9EbtUT01Q")
messaged = 'Хэй привет! Добро пожаловать в мир новых знакомств. Меня зовут Жандос и я постараюсь найти для тебя людей, которые в будущем могут стать твоими верными друзьями, потому что друзья-это один из важнейших факторов весёлой школьной жизни, что соответствует слогану кандидата в президенты Ученического Совета Мады Абдрахмана: "Учёба только в радость". Ну а для этого давай узнаем чем ты интересуешься! Нажми на кнопку "Категорий"'

messageForMe = "Привет! Меня зовут Асылхан. Напиши мне и я создам бота, который нужен именно тебе! tg: @kaori_42 inst: @kaori_42"

text = '[Разработчик бота: Асылхан 11А /n Нужен бот,сайт, мобильное приложение или же игра? Напиши мне и ты получишь то, что нужно тебе!](https://t.me/kaori_42)'
App_Url = f'https://abdrbotnispresident.herokuapp.com/{tokenn}'
server = Flask(__name__)

@server.route('/'+ tokenn, methods = ['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url = App_Url)
    return '!' , 200

if __name__ == '__main__':
    server.run(host='0.0.0.0' , port = int(os.environ.get('PORT' , 5000)))


def tele_vot():
    

    @bot.message_handler(commands = ["start"])
    def start_message(message):
        bot.send_message(message.chat.id ,messaged)
       
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Категорий")
        btn2 = types.KeyboardButton("Заказать своего бота")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id ,text, parse_mode='Markdown' ,reply_markup=markup)
        
    @bot.message_handler(commands = ["Next"])
    def start(message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Игры🎮", url='https://t.me/+x3SRz_9NlHtlODYy')
        button2 = types.InlineKeyboardButton("CS:GO🎮", url='https://t.me/+tKnB3F9mPXA0YWFi')
        button3 = types.InlineKeyboardButton("DOTA🎮", url='https://t.me/+hjlq_z4ykhE2MGRi')
        button4 = types.InlineKeyboardButton("Математика🔢", url='https://t.me/+oa8lH45TWBI5MWRi')
        button5 = types.InlineKeyboardButton("Биология🔬", url='https://t.me/+KSLUHyjQEl5jMzg6')
        button6 = types.InlineKeyboardButton("Химия🧪", url='https://t.me/+EsTGDXO9CaMzNWQy')
        button7 = types.InlineKeyboardButton("Физика🔌", url='https://t.me/+UzxVXYmDOdYxMWMy')
        button8 = types.InlineKeyboardButton("Аниме🏯", url='https://t.me/+SlT3ABQnoAJlM2Ji')
        button9 = types.InlineKeyboardButton("Дорамы🥢", url='https://t.me/+uK1wXvJYUIthY2Ji')
        button10 = types.InlineKeyboardButton("Сериалы🎬", url='https://t.me/+koR8_9NfMM1jMDI6')
        button11 = types.InlineKeyboardButton("Фильмы🍿", url='https://t.me/+Iy8naQKnjnE0NmIy')
        button12 = types.InlineKeyboardButton("Спорт🏅", url='https://t.me/+vV6hRCab1WBmYWUy')
        button13 = types.InlineKeyboardButton("Баскетбол🏀", url='https://t.me/+U6OvlEKCYn0wNTNi')
        button14 = types.InlineKeyboardButton("Футбол⚽️", url='https://t.me/+JZmTFBGKrC85M2Zi')
        button15 = types.InlineKeyboardButton("Настольный теннис🏓", url='https://t.me/+Y17dgDxeM3w1YTY6')
        button16 = types.InlineKeyboardButton("Волейбол🏐", url='https://t.me/+V7Kp_JHG_atiMzgy')
        button17 = types.InlineKeyboardButton("Качалка💪", url='https://t.me/+zOwC8og_BBJkMjhi')
        button18 = types.InlineKeyboardButton("Интернат🏫", url='https://t.me/+Nf5cryP2sLo2OTYy')
        button19 = types.InlineKeyboardButton("Программирование👨‍💻", url='https://t.me/+GM2O_AHqDJc5MmFi')
        button20 = types.InlineKeyboardButton("Веб разработчик👨‍💻", url='https://t.me/+jNLBiGPK1so4M2I6')
        button21 = types.InlineKeyboardButton("Мобильный разработчик👨‍💻", url='https://t.me/+OnYx6jD2kosxM2My')
        button22 = types.InlineKeyboardButton("Гейм дев👨‍💻", url='https://t.me/+U4SF9YDRyqwxN2Ji')
        button23 = types.InlineKeyboardButton("Музыка🎵", url='https://t.me/+BRfwBjSYya5jOWEy')
        button24 = types.InlineKeyboardButton("Танцы🕺", url='https://t.me/+tI-mlggEyoNkMjgy')
        button25 = types.InlineKeyboardButton("Видеомонтажеры🎥", url='https://t.me/+QfzW0tOa63w5NmIy')
  
        markup.add(button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24, button25)
        bot.send_message(message.chat.id, "{0.first_name}, нажми на одну из кнопок и перейди в одну из интересующих тебя групп)".format(message.from_user), reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def func(message):
        if(message.text == "Категорий"):
            start(message)
            bot.send_message(message.chat.id ,text, parse_mode='Markdown' )
        elif(message.text == "Заказать своего бота"):
            bot.send_message(message.chat.id, messageForMe)
   
    bot.polling()

tele_vot()
    
