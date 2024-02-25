import json
import os
from brain import Brain


try:
    with open('bot_chat_scripts/main_msgs.json', 'r', encoding='utf-8') as main_msgs:
        main_msgs_data = json.load(main_msgs)
    with open('bot_chat_scripts/recipes_msgs.json', 'r', encoding='utf-8') as recipes_msgs:
        recipes_msgs_data = json.load(recipes_msgs)
    with open('bot_chat_scripts/main_interfaces.json', 'r', encoding='utf-8') as main_interfaces:
        keyboard_interfaces_data = json.load(main_interfaces)
except Exception as e:
    print('PrepareData4Foody', e)

try:
    foody = Brain(api_key=os.getenv('BotAPI'),
                  main_msgs=main_msgs_data, recipes_msgs=recipes_msgs_data,
                  keyboard_interfaces=keyboard_interfaces_data)
except Exception as e:
    print('FoodyBrainError:', e)
