import telebot
from telebot import types
import random
import time
import json

bot = telebot.TeleBot('6035859101:AAEjqd24_RcN8fblJ_ZsS6ZD1_T3s1a34BI')

chapter = {}

with open('bot_chat_scripts/main_msgs.json', 'r', encoding='utf-8') as fh:
    messages_data = json.load(fh)

with open('jcts.json', 'r', encoding='utf-8') as fh:
    jcts_data = json.load(fh)


@bot.message_handler(commands=['start'])
def start(message):
    global chapter
    chapter[message.from_user.id] = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("диабет 💉")
    item2 = types.KeyboardButton("ир 🩸")
    item3 = types.KeyboardButton("проблемы с жкт 💊")
    item4 = types.KeyboardButton("советы для всех 📝")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, '<b>Выбери подходящую категорию</b>', reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'диабет 💉')
def diabetes(message):
    global chapter
    chapter[message.from_user.id] = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("рацион на день")
    item2 = types.KeyboardButton("таблица ГИ")
    item3 = types.KeyboardButton("что можно ✅")
    item4 = types.KeyboardButton("что нельзя ❌")
    item5 = types.KeyboardButton("сахарозаменители")
    item6 = types.KeyboardButton("в главное меню →")
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, messages_data['diabetes_text'], reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'рацион на день')
def diet(message):
    try:
        if chapter[message.from_user.id] == 0 or chapter[message.from_user.id] == 1:
            breakfast_position = random.choice(list(jcts_data['breakfast_dia'].keys()))
            dinner_position = random.choice(list(jcts_data['dinner_dia'].keys()))
            supper_position = random.choice(list(jcts_data['supper_dia'].keys()))

            text_diet = "<b>Завтрак:</b>\n" \
                        f"{breakfast_position} → <a href='{jcts_data['breakfast_dia'][breakfast_position]}'>рецепт</a>\n\n" \
                        f"<b>Обед:</b>\n" \
                        f"{dinner_position} → <a href='{jcts_data['dinner_dia'][dinner_position]}'>рецепт</a>\n\n" \
                        f"<b>Ужин:</b>\n" \
                        f"{supper_position} → <a href='{jcts_data['supper_dia'][supper_position]}'>рецепт</a>"
            bot.send_message(message.chat.id, text_diet, parse_mode='html')
            bot.send_message(message.chat.id,
                             messages_data['services_info'][f'attensions_{chapter[message.from_user.id]}'],
                             parse_mode='html')

        elif chapter[message.from_user.id] == 2:
            bot.send_message(message.chat.id, messages_data['services_info']['attensions_2'], parse_mode='html')

            breakfast_position = random.choice(list(jcts_data['breakfast_jct'].keys()))
            dinner_position = random.choice(list(jcts_data['dinner_jct'].keys()))
            supper_position = random.choice(list(jcts_data['supper_jct'].keys()))

            text_diet = "<b>Завтрак:</b>\n" \
                        f"{breakfast_position} → <a href='{jcts_data['breakfast_jct'][breakfast_position]}'>рецепт</a>\n\n" \
                        f"<b>Обед:</b>\n" \
                        f"{dinner_position} → <a href='{jcts_data['dinner_jct'][dinner_position]}'>рецепт</a>\n\n" \
                        f"<b>Ужин:</b>\n" \
                        f"{supper_position} → <a href='{jcts_data['supper_jct'][supper_position]}'>рецепт</a>"
            bot.send_message(message.chat.id, text_diet, parse_mode='html')

    except KeyError:
        sorry_text = "<b>Извините, я запутался...</b> Попробуйте еще раз."
        bot.send_message(message.chat.id, sorry_text, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("диабет 💉")
        item2 = types.KeyboardButton("ир 🩸")
        item3 = types.KeyboardButton("проблемы с жкт 💊")
        item4 = types.KeyboardButton("советы для всех 📝")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, '<b>Выбери подходящую категорию</b>', reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'таблица ГИ')
def table_gi(message):
    with open('./images/table_gi.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, messages_data['services_info']['gi'])


@bot.message_handler(func=lambda message: message.text == 'что нельзя ❌')
def cannot(message):
    try:
        if chapter[message.from_user.id] == 0:
            bot.send_message(message.chat.id, messages_data['cannot_dia'], parse_mode='html')
        elif chapter[message.from_user.id] == 1:
            bot.send_message(message.chat.id, messages_data['cannot_irt'], parse_mode='html')
    except KeyError:
        sorry_text = "<b>Извините, я запутался...</b> Попробуйте еще раз."
        bot.send_message(message.chat.id, sorry_text, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("диабет 💉")
        item2 = types.KeyboardButton("ир 🩸")
        item3 = types.KeyboardButton("проблемы с жкт 💊")
        item4 = types.KeyboardButton("советы для всех 📝")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, '<b>Выбери подходящую категорию</b>', reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'ир 🩸')
def irt(message):
    global chapter
    chapter[message.from_user.id] = 1

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("рацион на день")
    item2 = types.KeyboardButton("таблица ГИ")
    item3 = types.KeyboardButton("что нельзя ❌")
    item4 = types.KeyboardButton("в главное меню →")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, messages_data['irt_text'], reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'в главное меню →')
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("диабет 💉")
    item2 = types.KeyboardButton("ир 🩸")
    item3 = types.KeyboardButton("проблемы с жкт 💊")
    item4 = types.KeyboardButton("советы для всех 📝")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, '<b>Выбери подходящую категорию</b>', reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'проблемы с жкт 💊')
def jct(message):
    global chapter
    chapter[message.from_user.id] = 2

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("рацион на день")
    item2 = types.KeyboardButton("про глютен")
    item3 = types.KeyboardButton("про лактозу")
    item4 = types.KeyboardButton("про сахар")
    item5 = types.KeyboardButton("в главное меню →")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, messages_data['jct_text'], reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'про глютен')
def gluten(message):
    bot.send_message(message.chat.id, messages_data['gluten_text'], parse_mode='html')
    with open('./images/gluten.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda message: message.text == 'советы для всех 📝')
def advices(message):
    global chapter
    chapter[message.from_user.id] = 3

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("базовые анализы")
    item2 = types.KeyboardButton("пей больше воды")
    item3 = types.KeyboardButton("правильно кушай")
    item4 = types.KeyboardButton("планируем рацион")
    item5 = types.KeyboardButton("витамины")
    item6 = types.KeyboardButton("в главное меню →")
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, messages_data['advices_text'], reply_markup=markup, parse_mode='html')


simple_messages = {
    'пей больше воды': 'drink_text',
    'правильно кушай': 'eating_text',
    'про лактозу': 'lactose_text',
    'про сахар': 'sugar_text',
    'сахарозаменители': 'sugar_dia',
    'что можно ✅': 'good_dia',
    'планируем рацион': ['services_info', 'planning']
}


@bot.message_handler(func=lambda message: message.text in simple_messages)
def send_simple_messages(message):
    message_key = simple_messages[message.text]
    if type(message_key) == 'list' and len(message_key) == 2:
        bot.send_message(message.chat.id, messages_data[message_key[0]][message_key[1]], parse_mode='html')
    else:
        bot.send_message(message.chat.id, messages_data[simple_messages[message.text]], parse_mode='html')


@bot.message_handler(func=lambda message: 'дефицит' in message.text)
def send_about_deficit(message):
    vitamin = message.text.split(' ')
    if vitamin == 'B':
        for B in [1, 2, 3, 5, 6, 7, 8, 9, 12]:
            bot.send_message(message.chat.id, messages_data['vitamins'][f'B_{B}'], parse_mode='html')
    else:
        bot.send_message(message.chat.id, str(messages_data['vitamins'][vitamin]), parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'витамины')
def vitamins(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("дефицит A")
    item2 = types.KeyboardButton("дефицит B")
    item3 = types.KeyboardButton("дефицит C")
    item4 = types.KeyboardButton("дефицит D")
    item5 = types.KeyboardButton("дефицит E")
    item6 = types.KeyboardButton("дефицит K")
    item7 = types.KeyboardButton("в главное меню →")
    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, messages_data['vitamins']['main'], reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'базовые анализы')
def analysis(message):
    bot.send_message(message.chat.id, messages_data['services_info']['analysis'], parse_mode='html')
    with open('./images/analysis.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


while True:
    try:
        bot.polling(non_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(5)
        continue
# bot.polling(none_stop=True, timeout=30, interval=0)
