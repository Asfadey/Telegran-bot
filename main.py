import telebot
from telebot import types

bot = telebot.TeleBot('6140710004:AAHN5l-7FGON_e6UuGBlhwmg9iXK5mCoe7k')
# Код для Телеграм-бота

# Код для команды Старт
@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup1 = types.KeyboardButton(text='Список услуг 🧾')
    markup2 = types.KeyboardButton(text='Контакты 📞')
    markup3 = types.KeyboardButton(text='Отзывы ⭐')
    markup4 = types.KeyboardButton(text='Помощь 💁‍♀️')
    markup5 = types.KeyboardButton(text='Поддержка 🎧')
    kb.add(markup1, markup2, markup3, markup4, markup5)
    bot.send_message(message.chat.id, 'Привет! Я телеграм-бот компании AsfaIT. \n \nЯ здесь, чтобы помочь тебе получить доступ к нашим IT услугам. Будь то разработка веб-сайтов, мобильных приложений или консультации по информационной безопасности, мы готовы поддержать тебя в твоем проекте. \n \nТы всегда можешь задать свой вопрос в нашу дружелюбную поддержку!', reply_markup=kb)

# Код для команды Помощь
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Вот список доступных команд:\n \n/start - начать работу с ботом\n/services - просмотреть список наших IT услуг\n/contact - получить контактную информацию для связи с нами\n/portfolio - ознакомиться с нашим портфолио\n/help - получить помощь по использованию бота\n/support - обратиться в службу поддержки для получения дополнительной помощи')

# Код для команды Сервисы
@bot.message_handler(commands=['services'])
def services(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Разработка сайтов', callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text='Разработка дизайна сайта', callback_data='btn2')
    btn3 = types.InlineKeyboardButton(text='Разработка Телеграм-ботов', callback_data='btn3')
    kb.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Список IT услуг, предостовляемых нашей командой:', reply_markup=kb)


# Код для команды Контакты
@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(message.chat.id, 'Ниже приведены наши контактные данные: \n \n ● Телефон: +X (XXX) XXX-XXXX \n ● Email: info@asfait.com \n ● Адрес: ул. Название, город, страна \n \nНе стесняйтесь связываться с нами по любым вопросам и запросам. Наша команда готова помочь вам в решении любых IT задач!')

# Код для команды Портфолио
@bot.message_handler(commands=['portfolio'])
def portfolio(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    port1 = types.InlineKeyboardButton(text='Посмотреть портфолио', url='https://www.youtube.com/')
    kb.add(port1)
    bot.send_message(message.chat.id, 'Здесь вы найдете информацию о наших компетенциях и опыте работы, которые помогут вам принять решение о сотрудничестве с нами.', reply_markup=kb)

# Код для команды Поддержка
@bot.message_handler(commands=['support'])
def support(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    sup1 = types.InlineKeyboardButton(text='Написать нашей поддержке', url='https://t.me/+LFvjHB7w7lBhZDEy')
    kb.add(sup1)
    bot.send_message(message.chat.id, 'Если у вас возникли вопросы по использованию наших услуг или вам нужна помощь в их настройке, пожалуйста, обратитесь к нашей службе поддержки.', reply_markup=kb)

# Код для ключевых слов
@bot.message_handler()
def words(message):
    if message.text == 'Помощь 💁‍♀️':
        bot.send_message(message.chat.id, 'Вот список доступных команд:\n \n/start - начать работу с ботом\n/services - просмотреть список наших IT услуг\n/contact - получить контактную информацию для связи с нами\n/portfolio - ознакомиться с нашим портфолио\n/help - получить помощь по использованию бота\n/support - обратиться в службу поддержки для получения дополнительной помощи')
    if message.text == 'Поддержка 🎧':
        kb = types.InlineKeyboardMarkup(row_width=1)
        sup1 = types.InlineKeyboardButton(text='Написать нашей поддержке', url='https://t.me/+LFvjHB7w7lBhZDEy')
        kb.add(sup1)
        bot.send_message(message.chat.id, 'Если у вас возникли вопросы по использованию наших услуг или вам нужна помощь в их настройке, пожалуйста, обратитесь к нашей службе поддержки.', reply_markup=kb)
    if message.text == 'Список услуг 🧾':
        kb = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Разработка сайтов', callback_data='btn1')
        btn2 = types.InlineKeyboardButton(text='Разработка дизайна сайта', callback_data='btn2')
        btn3 = types.InlineKeyboardButton(text='Разработка Телеграм-ботов', callback_data='btn3')
        kb.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Список IT услуг, предостовляемых нашей командой:', reply_markup=kb)
    if message.text == 'Отзывы ⭐':
        kb = types.InlineKeyboardMarkup(row_width=1)
        feed1 = types.InlineKeyboardButton(text='Посмотреть отзывы', url='https://t.me/+Cbb4reUcoIswMzQy')
        feed2 = types.InlineKeyboardButton(text='Оставить отзыв', url='https://t.me/+Cbb4reUcoIswMzQy')
        kb.add(feed1, feed2)
        bot.send_message(message.chat.id, 'Мы всегда рады получить ваше мнение о качестве наших IT услуг и услышать ваши отзывы и предложения. Пожалуйста, оставьте ваш отзыв, нажав на кнопку "Оставить отзыв" ниже. Ваше мнение очень важно для нас и поможет нам стать еще лучше!', reply_markup=kb)
    if message.text == 'Контакты 📞':
        bot.send_message(message.chat.id, 'Ниже приведены наши контактные данные: \n \n ● Телефон: +X (XXX) XXX-XXXX \n ● Email: info@asfait.com \n ● Адрес: ул. Название, город, страна \n \nНе стесняйтесь связываться с нами по любым вопросам и запросам. Наша команда готова помочь вам в решении любых IT задач!')

#Каллбеки
@bot.callback_query_handler(func=lambda callback: callback.data)
def check(callback):
    # Каллбек на Разработку сайтов
    if callback.data == 'btn1':
        kb = types.InlineKeyboardMarkup(row_width=3)
        site1 = types.InlineKeyboardButton(text='Сайт-визитка', callback_data='site')
        site2 = types.InlineKeyboardButton(text='Интернет-магазин', callback_data='site2')
        site3 = types.InlineKeyboardButton(text='Лэндинг', callback_data='site3')
        site4 = types.InlineKeyboardButton(text='Корпоративный сайт', callback_data='site4')
        site5 = types.InlineKeyboardButton(text='Хостинг сайтов', callback_data='site5')
        kb.add(site1, site2, site3, site4, site5)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тарифы на разработку сайтов, предостовляемых нашей командой:', reply_markup=kb)
    if callback.data == 'siteBack':
        kb = types.InlineKeyboardMarkup(row_width=3)
        site1 = types.InlineKeyboardButton(text='Сайт-визитка', callback_data='site')
        site2 = types.InlineKeyboardButton(text='Интернет-магазин', callback_data='site2')
        site3 = types.InlineKeyboardButton(text='Лэндинг', callback_data='site3')
        site4 = types.InlineKeyboardButton(text='Корпоративный сайт', callback_data='site4')
        site5 = types.InlineKeyboardButton(text='Хостинг сайтов', callback_data='site5')
        kb.add(site1, site2, site3, site4, site5)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тарифы на разработку сайтов, предостовляемых нашей командой:', reply_markup=kb)
    # Каллбек на Разработку дизайна сайта
    if callback.data == 'btn2':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Разработка дизайна сайта\n \n⏳Ожидается оплата', reply_markup=kb)
    # Каллбек на Разработку Телеграм-ботов
    if callback.data == 'btn3':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Разработка Телеграм бота\n \n⏳ Ожидается оплата', reply_markup=kb)
    # Каллбек на Сайт визитку
    if callback.data == 'site':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Разработка Сайта-визитки\n \n⏳ Ожидается оплата',
                         reply_markup=kb)
    # Каллбек на Интернет-магазин
    if callback.data =='site2':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Разработка Интернет-магазина\n \n⏳ Ожидается оплата', reply_markup=kb)
    # Каллбек на Лэндинг
    if callback.data == 'site3':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Разработка Лэндинга\n \n⏳ Ожидается оплата', reply_markup=kb)
    # Каллбек на Корпоротивный сайт
    if callback.data == 'site4':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Разработка Корпоротивного сайта\n \n⏳ Ожидается оплата',
                         reply_markup=kb)
    # Каллбек на хостинг сайтов
    if callback.data == 'site5':
        kb = types.InlineKeyboardMarkup(row_width=2)
        host1 = types.InlineKeyboardButton(text='Тариф XS - от 250тг/мес', callback_data='host1')
        host2 = types.InlineKeyboardButton(text='Тариф S - от 450тг/мес', callback_data='host2')
        host3 = types.InlineKeyboardButton(text='Тариф M - от 950тг/мес', callback_data='host3')
        host4 = types.InlineKeyboardButton(text='Тариф L - от 2 200тг/мес', callback_data='host4')
        host5 = types.InlineKeyboardButton(text='Тариф XL - от 4 900тг/мес', callback_data='host5')
        host6 = types.InlineKeyboardButton(text='Тариф XXL - от 6 800тг/мес', callback_data='host6')
        host7 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='siteBack')
        kb.add(host1, host2, host3, host4, host5, host6, host7)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Мы предоставляем надежный и быстрый хостинг для вашего сайта. У нас есть различные тарифные планы, подходящие для сайтов любого размера и типа. Мы гарантируем стабильность работы и высокую скорость загрузки вашего сайта.', reply_markup=kb)
    if callback.data == 'hostBack':
        kb = types.InlineKeyboardMarkup(row_width=2)
        host1 = types.InlineKeyboardButton(text='Тариф XS - от 250тг/мес', callback_data='host1')
        host2 = types.InlineKeyboardButton(text='Тариф S - от 450тг/мес', callback_data='host2')
        host3 = types.InlineKeyboardButton(text='Тариф M - от 950тг/мес', callback_data='host3')
        host4 = types.InlineKeyboardButton(text='Тариф L - от 2 200тг/мес', callback_data='host4')
        host5 = types.InlineKeyboardButton(text='Тариф XL - от 4 900тг/мес', callback_data='host5')
        host6 = types.InlineKeyboardButton(text='Тариф XXL - от 6 800тг/мес', callback_data='host6')
        host7 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='siteBack')
        kb.add(host1, host2, host3, host4, host5, host6, host7)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Мы предоставляем надежный и быстрый хостинг для вашего сайта. У нас есть различные тарифные планы, подходящие для сайтов любого размера и типа. Мы гарантируем стабильность работы и высокую скорость загрузки вашего сайта.', reply_markup=kb)
    # Каллбек на XS
    if callback.data == 'host1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        xs = types.InlineKeyboardButton(text='Заказать 💳', callback_data='xs1')
        xs2 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='hostBack')
        kb.add(xs, xs2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тариф XS включает в себя:\n \n ● Место на диске: 1GB SSD\n ● ОЗУ: 256МБ\n ● Просессор: 1 Ядро (30%)\n\nЦена от 250тг/мес', reply_markup=kb)
    # Каллбек на S
    if callback.data == 'host2':
        kb = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Заказать 💳', callback_data='s1')
        s2 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='hostBack')
        kb.add(s, s2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тариф S включает в себя:\n \n ● Место на диске: 2GB SSD\n ● ОЗУ: 516МБ\n ● Просессор: 1 Ядро (30%)\n\nЦена от 450тг/мес', reply_markup=kb)
    # Каллбек на M
    if callback.data == 'host3':
        kb = types.InlineKeyboardMarkup(row_width=1)
        m = types.InlineKeyboardButton(text='Заказать 💳', callback_data='m1')
        m2 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='hostBack')
        kb.add(m, m2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тариф M включает в себя:\n \n ● Место на диске: 5GB SSD\n ● ОЗУ: 768МБ\n ● Просессор: 1 Ядро (30%)\n\nЦена от 950тг/мес', reply_markup=kb)
    # Каллбек на L
    if callback.data == 'host4':
        kb = types.InlineKeyboardMarkup(row_width=1)
        l = types.InlineKeyboardButton(text='Заказать 💳', callback_data='l1')
        l2 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='hostBack')
        kb.add(l, l2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тариф L включает в себя:\n \n ● Место на диске: 12GB SSD\n ● ОЗУ: 1 024МБ\n ● Просессор: 2 Ядра (60%)\n\nЦена от 2 200тг/мес', reply_markup=kb)
    # Каллбек на XL
    if callback.data == 'host5':
        kb = types.InlineKeyboardMarkup(row_width=1)
        xl = types.InlineKeyboardButton(text='Заказать 💳', callback_data='xl1')
        xl2 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='hostBack')
        kb.add(xl, xl2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тариф XL включает в себя:\n \n ● Место на диске: 25GB SSD\n ● ОЗУ: 1 536МБ\n ● Просессор: 2 Ядра (80%)\n\nЦена от 4 900тг/мес', reply_markup=kb)
    # Каллбек на XXL
    if callback.data == 'host6':
        kb = types.InlineKeyboardMarkup(row_width=1)
        xxl = types.InlineKeyboardButton(text='Заказать 💳', callback_data='xxl1')
        xxl2 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='hostBack')
        kb.add(xxl, xxl2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Тариф XXL включает в себя:\n \n ● Место на диске: 50GB SSD\n ● ОЗУ: 2 048МБ\n ● Просессор: 2 Ядра (130%)\n\nЦена от 6 800тг/мес', reply_markup=kb)
    # Каллбек на Заказать хостинг
    # Каллбек на Заказать XS
    if callback.data == 'xs1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Хостинг сайта тарифа XS\n \n⏳ Ожидается оплата',
                         reply_markup=kb)
    # Каллбек на Заказать S
    if callback.data =='s1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Хостинг сайта тарифа S\n \n⏳ Ожидается оплата',
                         reply_markup=kb)
    # Каллбек на Заказать M
    if callback.data =='m1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Хостинг сайта тарифа M\n \n⏳ Ожидается оплата',
                         reply_markup=kb)
    # Каллбек на Заказать L
    if callback.data == 'l1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Хостинг сайта тарифа L\n \n⏳ Ожидается оплата',
                         reply_markup=kb)
    # Каллбек на Заказать XL
    if callback.data == 'xl1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Хостинг сайта тарифа XL\n \n⏳ Ожидается оплата',
                         reply_markup=kb)
    # Каллбек на Заказать XXL
    if callback.data == 'xl1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        design1 = types.InlineKeyboardButton(text='Оплатить', callback_data='design1')
        design2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='design2')
        kb.add(design1, design2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Услуга: Хостинг сайта тарифа XL\n \n⏳ Ожидается оплата',
                         reply_markup=kb)

bot.polling(none_stop=True)