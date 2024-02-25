import time
import telebot
from telebot import types
import random

class Brain:
    simple_messages = {
        'пей больше воды': 'drink_text',
        'правильно кушай': 'eating_text',
        'про лактозу': 'lactose_text',
        'про сахар': 'sugar_text',
        'сахарозаменители': 'sugar_dia',
        'что можно ✅': 'good_dia',
        'планируем рацион': ['services_info', 'planning']
    }

    page_relations = {
        'в главное меню →': [-1, 'main'],
        'ир 🩸': [1, 'irt'],
        'проблемы с жкт 💊': [2, 'jct'],
        'советы для всех 📝': [3, 'advices'],
        'витамины': [-1, 'vitamins'],
        'диабет 💉': [0, 'diabetes']
    }

    media_triggers = {
        'про глютен': ['gluten', 'gluten.png'],
        'таблица ГИ': ['gi', 'table_gi.png'],
        'базовые анализы': ['analysis', 'analysis.png']
    }

    def __init__(self, api_key:str, main_msgs:dict, recipes_msgs:dict, keyboard_interfaces:dict):
        self.bot = telebot.TeleBot(api_key)
        self.chapter = {}

        self.main_msgs = main_msgs
        self.recipes_msgs = recipes_msgs
        self.keyboard_interfaces = keyboard_interfaces

        self.__mainloop()

    def __mainloop(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.chapter[message.from_user.id] = 0

            markup = self.__prepare_interface('main')
            self.bot.send_message(message.chat.id, self.main_msgs['pages']['main'],
                                  reply_markup=markup, parse_mode='html')

        @self.bot.message_handler(func=lambda message: message.text in Brain.simple_messages)
        def send_simple_messages(message):
            message_key = Brain.simple_messages[message.text]
            if isinstance(message_key, list):
                self.bot.send_message(message.chat.id, self.main_msgs[message_key[0]][message_key[1]], parse_mode='html')
            else:
                self.bot.send_message(message.chat.id, self.main_msgs[message_key], parse_mode='html')

        @self.bot.message_handler(func=lambda message: 'дефицит' in message.text)
        def send_about_deficit(message):
            vitamin = message.text.split(' ')[1]
            if vitamin == 'B':
                for B in [1, 2, 3, 5, 6, 7, 8, 9, 12]:
                    self.bot.send_message(message.chat.id, self.main_msgs['vitamins'][f'B_{B}'], parse_mode='html')
            else:
                self.bot.send_message(message.chat.id, self.main_msgs['vitamins'][vitamin], parse_mode='html')

        @self.bot.message_handler(func=lambda message: message.text == 'что нельзя ❌')
        def cannot(message):
            try:
                chapter = self.chapter[message.from_user.id]
                self.bot.send_message(message.chat.id, self.main_msgs[f'cannot_{chapter}'], parse_mode='html')
            except KeyError:
                self.bot.send_message(message.chat.id, self.main_msgs['services_info']['sorry'], parse_mode='html')
                markup = self.__prepare_interface('main')
                self.bot.send_message(message.chat.id, self.main_msgs['pages']['main'], reply_markup=markup,
                                      parse_mode='html')


        @self.bot.message_handler(func=lambda message: message.text == 'рацион на день')
        def diet(message):
            try:
                diet_personal = 'dia'
                print(self.chapter[message.from_user.id])

                if self.chapter[message.from_user.id] in [0, 1]:
                    pass
                elif self.chapter[message.from_user.id] == 2:
                    diet_personal = 'jct'

                breakfast_position = random.choice(list(self.recipes_msgs[f'breakfast_{diet_personal}'].keys()))
                dinner_position = random.choice(list(self.recipes_msgs[f'dinner_{diet_personal}'].keys()))
                supper_position = random.choice(list(self.recipes_msgs[f'supper_{diet_personal}'].keys()))

                breakfast_position_url = self.recipes_msgs[f'breakfast_{diet_personal}'][breakfast_position]
                dinner_position_url = self.recipes_msgs[f'dinner_{diet_personal}'][dinner_position]
                supper_position_url = self.recipes_msgs[f'supper_{diet_personal}'][supper_position]

                text_diet = "<b>Завтрак:</b>\n" \
                            f"{breakfast_position} → <a href='{breakfast_position_url}'>рецепт</a>\n\n" \
                            f"<b>Обед:</b>\n" \
                            f"{dinner_position} → <a href='{dinner_position_url}'>рецепт</a>\n\n" \
                            f"<b>Ужин:</b>\n" \
                            f"{supper_position} → <a href='{supper_position_url}'>рецепт</a>"
                self.bot.send_message(message.chat.id, text_diet, parse_mode='html')
                self.bot.send_message(message.chat.id,
                                        self.main_msgs['services_info'][f'attensions_{self.chapter[message.from_user.id]}'],
                                        parse_mode='html')

            except Exception as e:
                print(e)

        @self.bot.message_handler(func=lambda message: message.text in Brain.page_relations)
        def load_page(message):
            page_config = Brain.page_relations[message.text]

            if page_config[0] != -1:
                self.chapter[message.from_user.id] = page_config[0]

            markup = self.__prepare_interface(page_config[1])
            self.bot.send_message(message.chat.id, self.main_msgs['pages'][page_config[1]],
                                    reply_markup=markup, parse_mode='html')

        @self.bot.message_handler(func=lambda message: message.text in Brain.media_triggers)
        def send_edu_media(message):
            media_config = Brain.media_triggers[message.text]
            self.bot.send_message(message.chat.id, self.main_msgs['media'][media_config[0]], parse_mode='html')
            with open(f'./images/{media_config[1]}', 'rb') as photo:
                self.bot.send_photo(message.chat.id, photo)

        while True:
            try:
                self.bot.polling(non_stop=True, interval=0)
            except Exception as e:
                print(e)
                time.sleep(5)
                continue

    def __prepare_interface(self, page:str):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_prepare = []

        for item, button in self.keyboard_interfaces[page].items():
            item = types.KeyboardButton(button)
            markup_prepare.append(item)
        markup.add(*markup_prepare)

        return markup