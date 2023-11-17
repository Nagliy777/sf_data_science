from telebot import types
import telebot

token = '6382762229:AAH9S2aeLp5EODnSWvXDXuCAMG0DFAYwPXc'
bot=telebot.TeleBot(token)
my_chat_id=1018174299

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1=types.KeyboardButton(text='Услуги')
    button2=types.KeyboardButton(text='О нас')
    button3=types.KeyboardButton(text='Оставить заявку')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Приветствую!', reply_markup=keyboard)
    
    
def send_request(message):
    mes=f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо,заявка принята')
    
def send_servive(message):
    bot.send_message(message.chat.id, '1. Купить пивко')
    bot.send_message(message.chat.id, '2. Купить рыбку')
    bot.send_message(message.chat.id, '3. Пивко и рыбку')
    
def info_func(message):
    keyboard=types.InlineKeyboardMarkup()
    url_button=types.InlineKeyboardButton(text='Перейти на Яндекс', url='https://ya.ru')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку и получишь результат.', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'о нас':
        info_func(message)
    if message.text.lower() == 'оставить заявку':
        bot.send_message(message.chat.id, 'Будем рады Вас обслужить, оставьте свои контактные данные.')
        bot.register_next_step_handler(message, send_request)
    if message.text.lower() == 'услуги':
        send_servive(message)
    

if __name__=='__main__':
    bot.infinity_polling()
