import telebot
from telebot import types
import random
import time

bot = telebot.TeleBot('6035859101:AAEjqd24_RcN8fblJ_ZsS6ZD1_T3s1a34BI')

chapter = {}

breakfast_dia = {
        'Омлет на кокосовом молоке со шпинатом': 'https://health-diet.ru/table_calorie_users/amp/2039125',
        'Творожок из зелёной гречки': 'https://www.iamcook.ru/showrecipe/19818',
        'Овсяная каша (из цельного зерна) на кокосовом масле/масле ГХИ с орехами': 'https://modernfamilycook.com/recipe-items/kasha-iz-tselnogo-ovsa',
        'Киноа + котлета из индейки и цукини + зелень (руккола, шпинат, зелёный лук)': 'https://kulinarenok.ru/kotlety-iz-indeyki-s-kabachkom-v-duhovke',
        'Боул с красной рыбой': 'https://www.edimdoma.ru/retsepty/143517-boul-s-zapechennym-lososem.amp',
        'Оладья из цукини + овощной салат + зелень': 'https://calorizator.ru/recipe/47684'
    }

dinner_dia = {
    'Пюре из нута + куриная котлета + овощи': 'https://www.gotovim.ru/sbs/bitochkurfarshnut.shtml',
    'Горбуша на овощной подушке': 'https://menunedeli.ru/recipe/gorbusha-v-multivarke-na-ovoshhnoj-podushke',
    'Фриттата с цуккини, шпинатом и томатами': 'https://menunedeli.ru/recipe/frittata-s-cukkini-shpinatom-i-tomatami',
    'Филе Палтуса + рис бурый + овощи': 'https://menunedeli.ru/recipe/file-paltusa-v-duxovke',
    'Шоколадный брауни из цукини': 'https://youtu.be/uFyMIKEqk5w',
    'Кокосовые кексы': 'https://youtu.be/ZRDANxgqJWc'
}

supper_dia = {
    'Скрембл из яиц и брокколи': 'http://oede.by/recipe/vtorye_blyuda/yajca__skrjembl',
    'Курица, запечённая с овощами': 'https://1000.menu/cooking/50341-pp-kurica-zapechennaya-s-ovoshchami-v-duxovke',
    'Белковый торт с куриным филе': 'https://chef.tm/recipe/336111/5_originalnyh_idej_dlya_belkovogo_uzhina',
    'Тушенные кальмары с овощами': 'https://menunedeli.ru/2011/05/tushenye-kalmary-s-lukom-i-morkovyu',
    'Рагу Рататуй': 'https://shkoladiabeta.ru/living/food/recipes/goryachee/ragu-ratatuy'
}

sugar_dia = "К сожалению, что ни говорили бы маркетологи, любые сахарозаменители противопоказаны людям с диабетом I/II типа. " \
            "Однако в редких случаях (на свой страх и риск) допускается употреблять в небольших количествах следующее:\n\n" \
            "▪️Сироп топинамбура \n" \
            "▪️Стевия (нельзя при расстройствах жкт) \n" \
            "▪️Эритрол/эритрит \n" \
            "▪️Сироп Агавы \n\n" \
            "Подробнее смотрите <a href='https://youtu.be/4qe9df8nIOU'>здесь</a>. "

diabetes_text = "При сахарном диабете I/II типа показаны 3-4 приема пищи в день с интервалом не менее 4 часов и не более 6 часов. " \
               "В промежутках между ними не допускаются перекусы, т.к. они способствуют резкому скачку сахара в крови.\n\n" \
               "Некомпетентные специалисты рекомендуют дробное питание, что категорически опасно для здоровья.\n" \
               "Подробнее прочитать можно <a href='https://worldclassmag.com/food/drobnoe-pitanie-pochemu-eto-vredno'>здесь</a>."

irt_text = "Инсулинорезистентность – это снижение восприимчивости инсулин-чувствительных тканей к действию инсулина при достаточной его концентрации в крови. " \
           "Подробнее в <a href='https://youtu.be/5T7sDJJm3Xo'>видео</a>.\n\n" \
           "<b>ПРИЧИНЫ:</b>\n" \
           "▪️Избыток простых углеводов и сахара\n" \
           "▪️Дробное питание (5-6 разовое)\n" \
           "▪️Постоянные перекусы\n" \
           "▪️Переизбыток фруктозы\n" \
           "▪️Поздний ужин\n\n" \
           "<b>СИМПТОМЫ:</b>\n" \
           "▪️Запоры, вздутие, газообразование\n" \
           "▪️Акне, шелушения\n" \
           "▪️Аутоиммунные заболевания\n" \
           "▪️Кандидоз\n" \
           "▪️Повышенное чувство тревоги и страха\n\n" \
           "<b>ПОСЛЕДСТВИЯ:</b>\n" \
           "▪️Лишний вес\n" \
           "▪️Сердечно-сосудистые заболевания\n" \
           "▪️Высокая вероятность инфаркта/инсульта\n" \
           "▪️Акне, жирный блеск кожи\n" \
           "▪️Выпадение волос\n" \
           "▪️Хроническая усталость\n"

jct_text = "Если желудочно-кишечный тракт функционирует нормально, то он исправно перерабатывает пищу для обеспечения организма необходимой ему энергией. " \
           "Но иногда в его работе происходит сбой, который становится причиной множества заболеваний желудочно-кишечного тракта и всего организма.\n\n" \
           "<b>К заболеваниям желудочно-кишечного тракта относятся:</b>\n\n" \
           "• Хронический гастрит (воспаление слизистой желудка)\n" \
           "• Язвенная болезнь желудка и двенадцатиперстной кишки\n" \
           "• Воспаление слизистой пищевода (эзофагит, гастроэзофагеальная рефлюксная болезнь)\n" \
           "• Хронический панкреатит (воспаление поджелудочной железы)\n" \
           "• Различные воспалительные процессы в печени (хронический гепатит)\n" \
           "• Воспаления желчного пузыря (хронический холецистит)\n" \
           "• Воспаление тонкого и толстого отделов кишечника (хронический колит и энтероколит)\n" \
           "• Дисбактериоз кишечника (нарушения микрофлоры кишечника)\n" \
           "• Ферментопатии у взрослых и детей"

cannot_dia = "<b>ПРОСТЫЕ УГЛЕВОДЫ:</b>\n" \
             "▪️Сахар\n" \
             "▪️Сиропы\n" \
             "▪️Сладкие йогурты\n" \
             "▪️Выпечка и хлебобулочные изделия\n" \
             "▪️Конфеты\n" \
             "▪️Газировки\n" \
             "▪️Переработанный рис\n" \
             "▪️Картофель\n" \
             "▪️Алкоголь\n" \
             "▪️Фаст фуд\n\n" \
             "<b>МОЛОЧНАЯ ПРОДУКЦИЯ:</b>\n" \
             "▪️Молоко\n" \
             "▪️Кефир\n\n" \
             "<b>ФРУКТЫ:</b>\n" \
             "▪️Арбуз\n" \
             "▪️Виноград\n" \
             "▪️Бананы\n" \
             "▪️Малина\n" \
             "▪️Изюм\n" \
             "▪️Дыня\n" \
             "▪️Киви\n\n" \
             "<b>МЯСНАЯ ПРОДУКЦИЯ:</b>\n" \
             "▪️Колбасы\n" \
             "▪️Сосиски\n" \
             "▪️Свинина\n" \
             "▪️Жирные сорта мяса"

cannot_irt = "❗️Категорически запрещено употреблять продукты с высоким ГИ (смотрите таблицу ГИ)\n\n" \
             "<b>И ЗАПОМНИТЕ, ЧТО ВАМ НЕЛЬЗЯ:</b>\n" \
             "▪️Сахар\n" \
             "▪️Сиропы\n" \
             "▪️Сладкие йогурты\n" \
             "▪️Выпечка и хлебобулочные изделия\n" \
             "▪️Конфеты\n" \
             "▪️Газировки\n" \
             "▪️Картофель\n" \
             "▪️Алкоголь\n" \
             "▪️Фаст фуд\n" \
             "▪️Молоко\n" \
             "▪️Жирные сыры\n" \
             "▪️Колбасы и сосиски\n\n" \
             "❗️Можно использовать натуральные низкокалорийные сахарозаменители\n"

good_dia = "<b>ФРУКТЫ И ЯГОДЫ:</b>\n" \
           "▪️Лимон\n" \
           "▪️Авокадо\n" \
           "▪️Клюева\n" \
           "▪️Крыжовник\n" \
           "▪️Красная смородина\n" \
           "▪️Малина\n" \
           "▪️Ежевика\n" \
           "▪️Клубника\n" \
           "▪️Яблоки\n\n" \
           "<b>ЖИРЫ:</b>\n" \
           "▪️Оливковое масло\n" \
           "▪️Миндальное масло\n" \
           "▪️Арахисовое масло\n" \
           "▪️Рыбий жир\n" \
           "▪️Печень трески\n\n" \
           "<b>БОБОВЫЕ:</b>\n" \
           "▪️Нут\n" \
           "▪️Фасоль\n" \
           "▪️Чечевица\n" \
           "▪️Горох\n\n" \
           "<b>ЛЮБЫЕ ОВОЩИ, КРОМЕ КАРТОФЕЛЯ</b>\n\n" \
           "<b>НЕЖИРНЫЕ МЯСО И РЫБА</b>\n\n" \
           "<b>ЯЙЦА</b>\n\n" \
           "<b>ГРИБЫ</b>\n\n"

advices_text = "Я подготовил для тебя несколько советов, которые помогут поддерживать здоровье в норме!"

drink_text = "Пить воду — одна из привычек, которую нужно прививать! Если вы не хотите пить, то это не значит, что вам она не нужна.\n\n" \
             "<b>ПРИЗНАКИ ТОГО, ЧТО ВЫ МАЛО ПЬЁТЕ:</b>\n" \
             "▪️Жажда и сухость во рту\n" \
             "▪️Моча темно-желтого цвета\n" \
             "▪️Нерегулярный стул\n" \
             "▪️Сухая кожа\n" \
             "▪️Боли в суставах\n" \
             "▪️Образование целлюлита\n" \
             "▪️Неприятный запах пота\n" \
             "▪️Преждевременное старение\n\n" \
             "❗️Норма воды в день: 30 мл на 1 кг"

eating_text = "Достаточно придерживаться простых правил во избежание проблем со здоровьем:\n\n" \
         "▪️Не ешьте на ходу/стоя\n" \
         "▪️Тщательно пережевывайте пищу (около 30 раз)\n" \
         "▪️Во время еды не пейте никакие напитки, кроме тёплой воды\n" \
         "▪️В каждый прием пищи включайте овощи и зелень\n" \
         "▪️Избегайте перекусов\n" \
         "▪️Не употребляйте в пищу лишь одни углеводы\n" \
         "▪️Старайтесь минимизировать употребление сахара\n"

breakfast_jct = {'Пшено-киноа с тыквой': 'https://www.gastronom.ru/recipe/amp/51510',
                 'Овсяная каша на кокосовом молоке': 'https://hi-chef.ru/recipe/13073-ovsjanaja-kasha-na-kokosovom-moloke',
                 'Пшенная каша на кокосовом молоке': 'https://lefood.menu/recipes/pshennaya-kasha-na-kokosovom-moloke',
                 'Амарантовая каша с тыквой': 'https://www.povarenok.ru/recipes/show/147701',
                 'Зелёная гречка на растительном молоке': 'https://pp-prozozh.ru/zelenaja-grechka-na-kokosovom-moloke.html',
                 'Омлет с авокадо': 'https://www.gastronom.ru/recipe/amp/45927'}

dinner_jct = {'Спагетти из чечевицы с баклажанами': 'https://vkusvill.ru/media/recipes/spagetti-iz-chechevitsy-s-baklazhanami.html',
              'Гречка с овощами': 'https://1000.menu/amp/cooking/29313-grechka-na-skovorode-s-ovoschami',
              'Боул с красной рыбой': 'https://www.edimdoma.ru/retsepty/143517-boul-s-zapechennym-lososem.amp',
              'Оладья из цукини + овощной салат + зелень': 'https://calorizator.ru/recipe/47684',
              'Рагу Рататуй': 'https://shkoladiabeta.ru/living/food/recipes/goryachee/ragu-ratatuy',
              'Горбуша на овощной подушке': 'https://menunedeli.ru/recipe/gorbusha-v-multivarke-na-ovoshhnoj-podushke'}

supper_jct = {'Творожок из зелёной гречки': 'https://www.iamcook.ru/showrecipe/19818',
              'Киноа + котлета из индейки и цукини + зелень (руккола, шпинат, зелёный лук)': 'https://kulinarenok.ru/kotlety-iz-indeyki-s-kabachkom-v-duhovke',
              'Скрембл из яиц и брокколи': 'http://oede.by/recipe/vtorye_blyuda/yajca__skrjembl',
              'Шоколадный брауни из цукини': 'https://youtu.be/uFyMIKEqk5w',
              'Кокосовые кексы': 'https://youtu.be/ZRDANxgqJWc',
              'Пюре из нута + куриная котлета + овощи': 'https://www.gotovim.ru/sbs/bitochkurfarshnut.shtml'}

gluten_text = "Глютен или клейковина – высокомолекулярный белок, который содержится в большинстве зерновых культур (особенно в пшенице, ржи и ячмене). Именно он придает выпечке тягучесть и эластичность.\n\n" \
              "Лидеры по содержанию глютена – это пшеница (80%) и манная крупа (50%). Дальше идут печенья и бисквиты (20-40 %), мороженое (до 20 %), овес (21%), геркулес (12 %), макароны (11%), колбасы (до 10 %). " \
              "Клейковина есть даже в сырах и йогуртах – примерно 1 % от общей массы.\n\n" \
              "❗️Глютен опасен тем, что может вызывать аллергию.\n\n" \
              "Попадая вместе с пищей в ЖКТ, вещество распадается на фракции. Одну из них, а именно глиадин, иммунная система воспринимает как чужеродный белок – и вырабатывает в ответ иммунные комплексы, которые повреждают стенки кишечника. " \
              "Тот, в свою очередь, воспаляется, атрофируется его слизистая, нарушается нормальное всасывание необходимых нутриентов. " \
              "Микроэлементы и полезные вещества не усваиваются организмом, а превращаются в продукты распада, отравляя его.\n\n" \
              "При разных болезнях ЖКТ следует исключать глютеносодержащие продукты  из своего рациона.\n\n" \
              "Подробнее <a href='https://blog.zdravcity.ru/glyuten-tak-li-strashen-chert-kak-ego-malyuyut/'>тут</a>"

lactose_text = "Лактоза — это углевод (известный как молочный сахар), содержащийся в молоке и молочных продуктах. Именно лактоза придаёт молоку сладкий вкус. " \
               "Во время пищеварения лактоза расщепляется с помощью лактаза - фермента, выделяемого выделяемого в тонком кишечнике." \
               "Фермент лактаза необходим для расщепления молочного сахара — лактозы.\n\n" \
               "Лактазная недостаточность — генетическая особенность каждого организма, которая не меняется в течение всей жизни.\n\n" \
               "❗️Лактазную недостаточность можно определить, сдав анализ слюны или крови.\n\n" \
               "<b>ВИДЫ ЛАКТАЗНОЙ НЕДОСТАТОЧНОСТИ:</b>\n\n" \
               "▪️Первичная (генотип С/С): исключается любое молоко: коровье, козье, овечье. Так как тонкий кишечник не синтезирует фермент лактазу\n\n" \
               "▪️Вторичная (генотип С/Т): исключается любое молоко на время болезней, связанных с влиянием на тонкий кишечник. " \
               "Так как в это время не вырабатывается лактаза. Признаки: акне, отеки, метеоризм\n\n" \
               "▪️Генотип Т/Т: хорошая переносимость лактозы.\n\n" \
               "❗️На время болезней жкт молоко строго исключается\n\n" \
               "<b>АЛЬТЕРНАТИВА ОБЫЧНОМУ МОЛОКУ:</b>\n\n" \
               "🥛Кокосовое молоко\n" \
               "🥛Миндальное молоко\n" \
               "🥛Кунжутное молоко\n" \
               "🥛Льняное молоко\n" \
               "🥛Конопляное молоко"

sugar_text = "Сахар должен полностью исключаться из рациона.\n\n" \
             "Нашему мозгу нужна ГЛЮКОЗА, а не сахар. Ее можно получить из любых углеводов — бобовые, крупы, овощи, зелень, ягоды, фрукты. Поэтому сахар нам вовсе и не нужен.\n\n" \
             "❗️Сахар вызывает зависимость. Со временем мозг становится толерантным к сахару и человек увеличивает потребление количества сахара.\n\n" \
             "<b>МИФ: ДЛЯ МОЗГА НУЖЕН САХАР</b>\n" \
             "Сахар вызывает кратковременный подъем уровня глюкозы в крови, наступает временный прилив энергии. " \
             "Однако после этого уровень глюкозы резко падает и возникает упадок сил. " \
             "Появляется желание прибегнуть к новой порции сладкого стимулятора.\n\n" \
             "❗️Сахар повреждает кишечник. Поэтому при заболеваниях жкт его употребление крайне опасно.\n\n" \
             "Рекомендую к просмотру документальный фильм: https://youtu.be/8f4R8u2b8IQ\n\n" \
             "Ссылка на исследование о вреде сахара: https://pubmed.ncbi.nlm.nih.gov/28835408/\n\n"

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

@bot.message_handler(func=lambda message: message.text=='диабет 💉')
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
    bot.send_message(message.chat.id, diabetes_text, reply_markup=markup, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='рацион на день')
def diet(message):
    try:
        if chapter[message.from_user.id] == 0 or chapter[message.from_user.id] == 1:
            breakfast_position = random.choice(list(breakfast_dia.keys()))
            dinner_position = random.choice(list(dinner_dia.keys()))
            supper_position = random.choice(list(supper_dia.keys()))

            text_diet = "<b>Завтрак:</b>\n" \
                        f"{breakfast_position} → <a href='{breakfast_dia[breakfast_position]}'>рецепт</a>\n\n" \
                        f"<b>Обед:</b>\n" \
                        f"{dinner_position} → <a href='{dinner_dia[dinner_position]}'>рецепт</a>\n\n" \
                        f"<b>Ужин:</b>\n" \
                        f"{supper_position} → <a href='{supper_dia[supper_position]}'>рецепт</a>"
            bot.send_message(message.chat.id, text_diet, parse_mode='html')

            if chapter[message.from_user.id] == 0:
                attentions = "<b>Внимание:</b> <i>Нельзя пропускать ни один приём пищи, в том числе и завтрак. " \
                             "Необходимо поесть в течение часа/полтора после пробуждения. " \
                             "До этого рекомендуется выпивать 1-2 стакана воды.\n\n" \
                             "Ужин должен содержать минимальное количество углеводов и калорий (не более 400).</i>"

                bot.send_message(message.chat.id, attentions, parse_mode='html')

            elif chapter[message.from_user.id] == 1:
                attentions = "<b>Внимание:</b> <i>Следует питаться 2-3 раза в день с интервалом от 4 до 7 часов. " \
                             "Избегайте перекусов в целях предотвращения резкого скачка инсулина в крови.\n\n" \
                             "Используйте таблицу ГИ для планирования своего рациона.\n\n" \
                             "Сахар — ваш враг. Старайтесь употреблять продукты на сахарозаменителях вместе с основным приемом пищи.</i>"

                bot.send_message(message.chat.id, attentions, parse_mode='html')

        elif chapter[message.from_user.id] == 2:
            attentions = "<b>Внимание:</b> <i>Чтобы точно понимать, какие продукты можно, а какие нельзя, нужно обязательно сдать анализы и проконсультироваться с врачом.\n\n" \
                         "Я предложу вам универсальные варианты блюд, которые подойдут при любом заболевании ЖКТ.</i>"

            bot.send_message(message.chat.id, attentions, parse_mode='html')

            breakfast_position = random.choice(list(breakfast_jct.keys()))
            dinner_position = random.choice(list(dinner_jct.keys()))
            supper_position = random.choice(list(supper_jct.keys()))

            text_diet = "<b>Завтрак:</b>\n" \
                        f"{breakfast_position} → <a href='{breakfast_jct[breakfast_position]}'>рецепт</a>\n\n" \
                        f"<b>Обед:</b>\n" \
                        f"{dinner_position} → <a href='{dinner_jct[dinner_position]}'>рецепт</a>\n\n" \
                        f"<b>Ужин:</b>\n" \
                        f"{supper_position} → <a href='{supper_jct[supper_position]}'>рецепт</a>"
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

@bot.message_handler(func=lambda message: message.text=='таблица ГИ')
def table_gi(message):
    with open('./images/table_gi.png', 'rb') as photo:
        gi_text = "ГИ — показатель, по которому оценивается скорость попадания глюкозы в кровь. " \
                  "Чем выше этот показатель, тем быстрее глюкоза попадает в кровь и тем более резким будет скачок ее уровня."
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, gi_text)

@bot.message_handler(func=lambda message: message.text=='что нельзя ❌')
def cannot(message):
    try:
        if chapter[message.from_user.id] == 0:
            bot.send_message(message.chat.id, cannot_dia, parse_mode='html')
        elif chapter[message.from_user.id] == 1:
            bot.send_message(message.chat.id, cannot_irt, parse_mode='html')
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

@bot.message_handler(func=lambda message: message.text=='что можно ✅')
def good(message):
    bot.send_message(message.chat.id, good_dia, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='сахарозаменители')
def sugar(message):
    bot.send_message(message.chat.id, sugar_dia, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='ир 🩸')
def irt(message):
    global chapter
    chapter[message.from_user.id] = 1

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("рацион на день")
    item2 = types.KeyboardButton("таблица ГИ")
    item3 = types.KeyboardButton("что нельзя ❌")
    item4 = types.KeyboardButton("в главное меню →")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, irt_text, reply_markup=markup, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='в главное меню →')
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("диабет 💉")
    item2 = types.KeyboardButton("ир 🩸")
    item3 = types.KeyboardButton("проблемы с жкт 💊")
    item4 = types.KeyboardButton("советы для всех 📝")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, '<b>Выбери подходящую категорию</b>', reply_markup=markup, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='проблемы с жкт 💊')
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
    bot.send_message(message.chat.id, jct_text, reply_markup=markup, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='про глютен')
def gluten(message):
    bot.send_message(message.chat.id, gluten_text, parse_mode='html')
    with open('./images/gluten.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda message: message.text=='про лактозу')
def lactose(message):
    bot.send_message(message.chat.id, lactose_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='про сахар')
def sugar(message):
    bot.send_message(message.chat.id, sugar_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='советы для всех 📝')
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
    bot.send_message(message.chat.id, advices_text, reply_markup=markup, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='пей больше воды')
def drink(message):
    bot.send_message(message.chat.id, drink_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='правильно кушай')
def eating(message):
    bot.send_message(message.chat.id, eating_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='планируем рацион')
def planning(message):
    planning_text = "Я подобрал для тебя несколько советов, которые помогут разнообразить здоровый рацион.\n\n" \
                    "▪️Яйца могут быть через день\n" \
                    "▪️Красное мясо — 2 раза в неделю\n" \
                    "▪️Птица — 3 раза в неделю\n" \
                    "▪️Рыба, морепродукты — 2 раза в неделю (можно чаще)\n" \
                    "▪️Обязательно включай в рацион субпродукты (печень, сердечки)\n" \
                    "▪️Каждый день включай разные злаки и бобовые (если разрешены в лечебном протоколе питания)\n" \
                    "▪️Каждый день новый овощ, зелень (например, различные виды капусты и т.д.)"

    bot.send_message(message.chat.id, planning_text, parse_mode='html')
        
@bot.message_handler(func=lambda message: message.text=='витамины')
def vitamins(message):
    vitamins_text = "Внимание! Данный материал носит справочный характер\n\n" \
                    "Витамины, которые необходимы человеку, делятся на жирорастворимые:\n\n" \
                    "▪️А (ретинол)\n" \
                    "▪️D (колекальциферол)\n" \
                    "▪️E (токоферол)\n" \
                    "▪️К (филлохинон)\n\n" \
                    "и водорастворимые:\n\n" \
                    "▪️С (аскорбиновая кислота)\n" \
                    "▪️8 витаминов, объединенных в группу В: В1 (тиамин), В2 (рибофлавин), " \
                    "В3 (ниацин), В5 (пантотеновая кислота), В6 (пиридоксин), В7 (биотин), В9 (фолиевая кислота), В12 (кобаламин).\n\n" \
                    "Организм не в состоянии синтезировать их самостоятельно в достаточных количествах, поэтому получает их из пищи.\n\n" \
                    "НЕДОСТАТОК ВИТАМИНОВ ПРИВОДИТ:\n" \
                    "⁃ к ослаблению иммунитета,\n" \
                    "⁃ появлению разнообразных болезней,\n" \
                    "⁃ нарушению обмена веществ,\n" \
                    "⁃ излишней полноте,\n" \
                    "⁃ преждевременному старению.\n\n" \
                    "❗️Организму не нужно много витаминов! Свою норму он берет из продуктов." \
                    "Принимать дополнительно витамины в таблетках следует только при их дефиците!\n\n" \
                    "Подробнее можно узнать по <a href='https://gcmp.ru/doc_vitarole/'>ссылке</a>"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("дефицит A")
    item2 = types.KeyboardButton("дефицит B")
    item3 = types.KeyboardButton("дефицит C")
    item4 = types.KeyboardButton("дефицит D")
    item5 = types.KeyboardButton("дефицит E")
    item6 = types.KeyboardButton("дефицит K")
    item7 = types.KeyboardButton("в главное меню →")
    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, vitamins_text, reply_markup=markup, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='дефицит A')
def d_A(message):
    d_A_text = "Признаки дефицита витамина А в твоём организме:\n\n" \
               "▪️Сухие волосы\n" \
               "▪️Сухая кожа лица, угревая сыпь\n" \
               "▪️Сухость кожи рук\n" \
               "▪️Желтоватые ладони рук\n" \
               "▪️Нарушение адаптации глаз в темноте\n" \
               "▪️Болезни глаз\n" \
               "▪️Снижение именной защиты организма\n" \
               "▪️Нарушение обмена веществ\n\n" \
               "Продукты питания, богатые витамином А:\n\n" \
               "▪️Морковь\n" \
               "▪️Тыква\n" \
               "▪️Сладкий перец\n" \
               "▪️Шпинат\n" \
               "▪️Брокколи\n" \
               "▪️Зелёный лук\n" \
               "▪️Яблоки, абрикосы, дыня\n" \
               "▪️Рыбий жир\n" \
               "▪️Печень (особенно говяжья)\n\n" \
               "❗️БАДы назначаются только в случае дефицитов и только специалистом"

    bot.send_message(message.chat.id, d_A_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='дефицит C')
def d_C(message):
   d_C_text = "Признаки дефицита витамина С в твоём организме:\n\n" \
         "▪️Непроизвольные движения\n" \
         "▪️Параноидальные мысли\n" \
         "▪️Кровоточивость дёсен\n" \
         "▪️Отдышка\n" \
         "▪️Слабый иммунитет\n" \
         "▪️Плохое заживление ран\n" \
         "▪️Быстрая усталость\n\n" \
         "Продукты питания, богатые витамином С:\n\n" \
         "▪️Болгарский перец\n" \
         "▪️Цитрусовые фрукты\n" \
         "▪️Лимон\n" \
         "▪️Авокадо\n" \
         "▪️Зеленые овощи\n" \
         "▪️Брокколи, брюссельская капуста\n" \
         "▪️Ягоды\n\n" \
         "❗️БАДы назначаются только в случае дефицитов и только специалистом"

   bot.send_message(message.chat.id, d_C_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='дефицит D')
def d_D(message):
    d_D_text = "Признаки дефицита витамина D в твоём организме:\n\n" \
          "▪️Снижение настроения, депрессия\n" \
          "▪️Ухудшение состояния ногтевой пластины\n" \
          "▪️Судороги в мышцах\n" \
          "▪️Нарушение менструального цикла у женщин\n" \
          "▪️Потливость рук\n" \
          "▪️Повышенная ломкость волос\n\n" \
          "Продукты питания, богатые витамином D:\n\n" \
          "▪️Жирная рыба\n" \
          "▪️Растительное масло\n" \
          "▪️Куриные яйца\n" \
          "▪️Молочные продукты\n\n" \
          "❗️БАДы назначаются только в случае дефицитов и только специалистом"

    bot.send_message(message.chat.id, d_D_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='дефицит E')
def d_E(message):
    d_E_text = "Признаки дефицита витамина E в твоём организме:\n\n" \
          "▪️Слабость, усталость\n" \
          "▪️Быстрая утомляемость\n" \
          "▪️Снижение мыслительной деятельности\n" \
          "▪️Ломота в теле\n" \
          "▪️Пигментные пятна на коже\n" \
          "▪️Ранние морщины\n\n" \
          "Продукты питания, богатые витамином Е:\n\n" \
          "▪️Подсолнечное масло\n" \
          "▪️Орехи, семена\n" \
          "▪️Авокадо\n" \
          "▪️Паприка\n" \
          "▪️Печень\n" \
          "▪️Оливки\n" \
          "▪️Яичный желток\n\n" \
          "❗️БАДы назначаются только в случае дефицитов и только специалистом"

    bot.send_message(message.chat.id, d_E_text, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='дефицит K')
def d_K(message):
        d_K_text = "Признаки дефицита витамина К в твоём организме:\n\n" \
              "▪️Кровотечения из носа\n" \
              "▪️Кровоточивость дёсен\n" \
              "▪️Кровотечение в ЖКТ\n" \
              "▪️Кровь в моче\n" \
              "▪️Обильное менструальное кровотечение у женщин\n" \
              "▪️Искривление спины\n" \
              "▪️Переломы\n\n" \
              "Продукты питания, богатые витамином К:\n\n" \
              "▪️Брокколи\n" \
              "▪️Капуста\n" \
              "▪️Зеленые листовые овощи\n" \
              "▪️Шиповник\n" \
              "▪️Овёс\n" \
              "▪️Фасоль\n\n" \
              "❗️БАДы назначаются только в случае дефицитов и только специалистом"
        
        bot.send_message(message.chat.id, d_K_text, parse_mode='html')
        
@bot.message_handler(func=lambda message: message.text=='дефицит B')
def d_B(message):
    d_B_1 = "<b>B1</b>\n\n" \
             "Признаки дефицита витамина B1 в твоём организме:\n\n" \
             "▪️Судороги в ногах\n" \
             "▪️Апатия, депрессия\n" \
             "▪️Дезориентация\n" \
             "▪️Потеря зрения\n" \
             "▪️Слабость\n\n" \
             "Продукты питания, богатые витамином В1:\n\n" \
             "▪️Рыба\n" \
             "▪️Печень\n" \
             "▪️Говядина, свинина\n" \
             "▪️Яичный желток\n" \
             "▪️Орехи\n" \
             "▪️Спаржа\n" \
             "▪️Бобовые продукты" \

    bot.send_message(message.chat.id, d_B_1, parse_mode='html')

    d_B_2 = "<b>B2</b>\n\n" \
             "Признаки дефицита витамина В2 в твоём организме:\n\n" \
             "▪️Мигрень\n" \
             "▪️Зуд в глазах\n" \
             "▪️Трещины в уголках рта\n" \
             "▪️Трещины на губах\n" \
             "▪️Красное горло\n\n" \
             "Продукты питания, богатые витамином В2:\n\n" \
             "▪️Субпродукты\n" \
             "▪️Яйца\n" \
             "▪️Рыба\n" \
             "▪️Спаржа\n" \
             "▪️Бананы" \
        
    bot.send_message(message.chat.id, d_B_2, parse_mode='html')

    d_B_3 = "<b>B3</b>\n\n" \
            "Признаки дефицита витамина В3 в твоём организме:\n\n" \
            "▪️Раздражительность, депрессия\n" \
            "▪️Бессонница\n" \
            "▪️Головокружение\n" \
            "▪️Слабость\n" \
            "▪️Стоматит\n" \
            "▪️Онемение и покалывание рук\n" \
            "▪️Боли в животе\n\n" \
            "Продукты питания, богатые витамином В3:\n\n" \
            "▪️Субпродукты\n" \
            "▪️Цыплёнок\n" \
            "▪️Говядина\n" \
            "▪️Рыба\n" \
            "▪️Листовые овощи\n" \
            "▪️Морковь\n" \
            "▪️Томаты\n" \
            "▪️Спаржа\n" \
            "▪️Орехи" \

    bot.send_message(message.chat.id, d_B_3, parse_mode='html')

    d_B_5 = "<b>B5</b>\n\n" \
            "Признаки дефицита витамина В5 в твоём организме:\n\n" \
            "▪️Головная боль\n" \
            "▪️Выпадение волос\n" \
            "▪️Плохое заживление ран\n" \
            "▪️Артрит\n" \
            "▪️Пониженный иммунитет\n\n" \
            "Продукты питания, богатые витамином В5:\n\n" \
            "▪️Мясо с низким содержанием жира\n" \
            "▪️Субпродукты\n" \
            "▪️Яичный желток\n" \
            "▪️Зелёные листовые овощи\n" \
            "▪️Кукуруза\n" \
            "▪️Корнеплоды\n" \
            "▪️Авокадо\n" \
            "▪️Орехи" \
        
    bot.send_message(message.chat.id, d_B_5, parse_mode='html')

    d_B_6 = "<b>B6</b>\n\n" \
            "Признаки дефицита витамина В6 в твоём организме:\n\n" \
            "▪️Нервозность, раздражительность\n" \
            "▪️Неврит\n" \
            "▪️Депрессивное настроение\n" \
            "▪️Усталость\n" \
            "▪️Трещины на губах\n" \
            "▪️Трещины в уголках рта\n" \
            "▪️Онемение конечностей\n" \
            "▪️Чрезмерное дыхание\n" \
            "▪️ПМС у женщин\n\n" \
            "Продукты питания, богатые витамином В6:\n\n" \
            "▪️Мясо\n" \
            "▪️Яйца\n" \
            "▪️Рыба\n" \
            "▪️Печень\n" \
            "▪️Морковь\n" \
            "▪️Шпинат\n" \
            "▪️Авокадо\n" \
            "▪️Капуста\n" \
            "▪️Бананы\n" \
            "▪️Орехи" \

    bot.send_message(message.chat.id, d_B_6, parse_mode='html')

    d_B_7 = "<b>B7</b>\n\n" \
            "Признаки дефицита витамина В7 в твоём организме:\n\n" \
            "▪️Вялость, апатия\n" \
            "▪️Депрессия\n" \
            "▪️Галлюцинации (в тяжёлых случаях)\n" \
            "▪️Выпадение волос, облысение\n" \
            "▪️Конъюнктивит\n" \
            "▪️Мышечная боль\n" \
            "▪️Покалывание и онемение рук\n\n" \
            "Продукты питания, богатые витамином В7:\n\n" \
            "▪️Мясо\n" \
            "▪️Яйца\n" \
            "▪️Морская рыба\n" \
            "▪️Бобовые\n" \
            "▪️Молочка" \
        
    bot.send_message(message.chat.id, d_B_7, parse_mode='html')

    d_B_8 = "<b>B8</b>\n\n" \
            "Признаки дефицита витамина В8 в твоём организме:\n\n" \
            "▪️Депрессия\n" \
            "▪️Беспокойство\n" \
            "▪️Панические атаки\n" \
            "▪️Навязчивые мысли\n" \
            "▪️Повышенный уровень сахара в крови\n" \
            "▪️Невосприимчивость инсулина\n" \
            "▪️Нарушение менструального цикла у женщин\n" \
            "▪️Повышенный уровень тестостерона у женщин\n\n" \
            "Продукты питания, богатые витамином B8\n\n" \
            "▪️Проросшее зерно\n" \
            "▪️Замоченные орехи\n" \
            "▪️Фрукты" \

    bot.send_message(message.chat.id, d_B_8, parse_mode='html')

    d_B_9 = "<b>B9</b>\n\n" \
            "Признаки дефицита витамина В9 в твоём организме:\n\n" \
            "▪️Раздражительность, депрессия\n" \
            "▪️Забывчивость\n" \
            "▪️Умеренная усталость\n" \
            "▪️Бледная кожа\n" \
            "▪️Диарея\n\n" \
            "Продукты питания, богатые витамином B9:\n\n" \
            "▪️Печень\n" \
            "▪️Яйца\n" \
            "▪️Лосось\n" \
            "▪️Устрицы\n" \
            "▪️Зеленые листовые овощи\n" \
            "▪️Молочка\n" \
            "▪️Хлеб из цельного зерна" \
        
    bot.send_message(message.chat.id, d_B_9, parse_mode='html')

    d_B_12 = "<b>B12</b>\n\n" \
            "Признаки дефицита витамина В12 в твоём организме:\n\n" \
            "▪️Нарушение функций ЖКТ\n" \
            "▪️Раздражительность\n" \
            "▪️Плохая концентрация\n" \
            "▪️Несобранность\n" \
            "▪️Быстрое утомление, слабость\n\n" \
            "Продукты питания, богатые витамином В12:\n\n" \
            "▪️Печень, почки\n" \
            "▪️Диетическое мясо\n" \
            "▪️Морепродукты\n" \
            "▪️Яйца\n" \
            "▪️Молочка" \

    bot.send_message(message.chat.id, d_B_12, parse_mode='html')

@bot.message_handler(func=lambda message: message.text=='базовые анализы')
def analysis(message):
    analysis_text = "Я приготовил для тебя список базовых анализов, " \
                    "которые необходимо сдавать ежегодно для поддержания своего здоровья."

    bot.send_message(message.chat.id, analysis_text, parse_mode='html')
    with open('./images/analysis.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
        
while True:
    try:
        bot.polling(non_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(5)
        continue
#bot.polling(none_stop=True, timeout=30, interval=0)
