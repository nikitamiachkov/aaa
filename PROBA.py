import telebot as tb
from telebot import types as tp

bot = tb.TeleBot("6606735642:AAEPfRbSJb8NydIu3CmQ7dlW8CfofeCWCdk") 

@bot.message_handler(commands=['info'])
def start(message):
    bottom_1 = tp.InlineKeyboardMarkup()
    bottom_1.add(tp.InlineKeyboardButton("В меню", callback_data="menu"))
    bot.send_message(message.chat.id, f"Главные команды: \n  /info - информация о проекте \n  /donate - поддержать проект \n\n", reply_markup=bottom_1)

@bot.message_handler(commands=['clear'])
def clear(message):
    for i in range(message.message_id, 5, -1):
        bot.delete_message(message.from_user.id, i)

@bot.message_handler(commands=['start'])
def start(message):
    bottom_1 = tp.ReplyKeyboardMarkup(resize_keyboard=True)
    bottom_1.add(tp.InlineKeyboardButton("Что этот бот делает?"))
    bot.send_message(message.chat.id, "Приветствую тебя в качалочном храме!", reply_markup=bottom_1)
    bot.register_next_step_handler(message, on_what_click)
    print(message.message_id)

def on_what_click(message):
    if message.text == "Что этот бот делает?":
        bottom_2 = tp.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard=True)
        bottom_2.add(tp.InlineKeyboardButton("Список просвящённых качков"))
        bottom_2.add(tp.InlineKeyboardButton("Поддержать проект"))
#        bot.send_message(message.chat.id, "Это долгая история...", reply_markup=tp.ReplyKeyboardRemove()) 
        bot.send_message(message.chat.id, f"<i>Это долгая история...</i> Об этом месте слагают легенды: \n\n В стародавние времена группа единомышленников собралась, чтобы познать все качалочные тайны и поделиться ими с последователями.", reply_markup=bottom_2, parse_mode="html")
        bot.register_next_step_handler(message, witch)
    else:
        bot.send_message(message.chat.id, "Я не понимаю тебя, мой друг")
        bot.register_next_step_handler(message, on_what_click)

def witch(message):
    if message.text == "Список просвящённых качков" or message.text == "Вернуться":
        print("rkmfm")
        bottom_3 = tp.InlineKeyboardMarkup()
        bottom_3.add(tp.InlineKeyboardButton("Никита", callback_data="nikita"))
        bottom_3.add(tp.InlineKeyboardButton("Данил", callback_data="danil"))
        bottom_3.add(tp.InlineKeyboardButton("Вернуться", callback_data="menu"))
        bot.send_message(message.chat.id, "Вот наша гордость:", reply_markup=bottom_3)
    elif message.text.lower() == "поддержать проект":
        bottom_mon = tp.InlineKeyboardMarkup()
        bottom_mon.add(tp.InlineKeyboardButton("Вернуться", callback_data="money"))
        bot.send_message(message.chat.id, f"Номер карты: 3412 3459 9999 **** \n\nКопим на ампулы с тестостероном", reply_markup=bottom_mon, parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Я не понимаю тебя, мой друг")
        bot.register_next_step_handler(message, witch)

@bot.message_handler(commands=['donate'])
def donait(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    bottom_mon = tp.InlineKeyboardMarkup()
    bottom_mon.add(tp.InlineKeyboardButton("Вернуться", callback_data="menu"))
    bot.send_message(message.chat.id, f"Номер карты: 3412 3459 9999 **** \n\nКопим на ампулы с тестостероном", reply_markup=bottom_mon, parse_mode="html")

@bot.callback_query_handler(func=lambda callback: True)
def nikita(callback):
    if callback.data == "money":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bottom_2 = tp.InlineKeyboardMarkup()
        bottom_2.add(tp.InlineKeyboardButton("Список просвящённых качков", callback_data="back_menu"))
        bottom_2.add(tp.InlineKeyboardButton("Поддержать проект", callback_data= "mon2"))
        bot.send_message(callback.message.chat.id, "Спасибо за интерес!", reply_markup=bottom_2)
        print("1")
    elif callback.data == "menu":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bottom_2 = tp.InlineKeyboardMarkup()
        bottom_2.add(tp.InlineKeyboardButton("Список просвящённых качков", callback_data="back_menu"))
        bottom_2.add(tp.InlineKeyboardButton("Поддержать проект", callback_data= "mon3"))
        bot.send_message(callback.message.chat.id, "Меню: ", reply_markup=bottom_2)
        print("7")
    elif callback.data == "nikita":
        file = open("Nikita.png", "rb")
        bottom_n1 = tp.InlineKeyboardMarkup()
        bottom_n1.add(tp.InlineKeyboardButton("Вернуться", callback_data="back"))
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_photo(callback.message.chat.id, file, reply_markup=bottom_n1, caption=f"<b>Никита</b>, 17 лет \n\n<b>Жим: </b>1086кг\n<b>Становая: </b>99.999кг\n<b>Присед:</b> -100кг", parse_mode="html")
        print("2")
 #       return nikita(callback)
    elif callback.data == "danil":
        file = open("danil.jpg", "rb")  
        bottom_n1 = tp.InlineKeyboardMarkup()
        bottom_n1.add(tp.InlineKeyboardButton("Вернуться", callback_data="back"))
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_photo(callback.message.chat.id, file, reply_markup=bottom_n1, caption=f"<b>Данил</b>, 19 лет \n\n<b>Жим: </b>105кг\n<b>Становая: </b>160кг\n<b>Присед:</b> 140кг", parse_mode="html")
        print("3")
    elif callback.data == "back_menu":
        bottom_3 = tp.InlineKeyboardMarkup()
        bottom_3.add(tp.InlineKeyboardButton("Никита", callback_data="nikita"))
        bottom_3.add(tp.InlineKeyboardButton("Данил", callback_data="danil"))
        bottom_3.add(tp.InlineKeyboardButton("Вернуться", callback_data="menu"))
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Вот наша гордость:", reply_markup=bottom_3)
        print("6")
    elif callback.data == "back":
        bottom_3 = tp.InlineKeyboardMarkup()
        bottom_3.add(tp.InlineKeyboardButton("Никита", callback_data="nikita"))
        bottom_3.add(tp.InlineKeyboardButton("Данил", callback_data="danil"))
        bottom_3.add(tp.InlineKeyboardButton("Вернуться", callback_data="menu"))
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Вот наша гордость:", reply_markup=bottom_3)
        print("4")
    elif callback.data == "mon2":
        bottom_mon = tp.InlineKeyboardMarkup()
        bottom_mon.add(tp.InlineKeyboardButton("Вернуться", callback_data="money"))
        bot.send_message(callback.message.chat.id, "Номер карты: 3412 3459 9999 **** \n\nКопим на ампулы с тестостероном", reply_markup=bottom_mon, parse_mode="html")
    elif callback.data == "mon3":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bottom_mon = tp.InlineKeyboardMarkup()
        bottom_mon.add(tp.InlineKeyboardButton("Вернуться", callback_data="menu"))
        bot.send_message(callback.message.chat.id, "Номер карты: 3412 3459 9999 **** \n\nКопим на ампулы с тестостероном", reply_markup=bottom_mon, parse_mode="html")
    else:
        bot.send_message(callback.message.chat.id, "Я не понимаю тебя, мой друг")

    if callback.data == "money" or callback.data == "back":
        print("5")
        return nikita(callback)


bot.polling(none_stop = True)