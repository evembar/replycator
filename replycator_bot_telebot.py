print('Replycator BOT 0.01')

import telebot, random, os, replycator_api, sys, shutil
from telebot import types
from cfg import telegram_api as tgapi

bot_api = tgapi.telegram_api

bot = telebot.TeleBot(bot_api, parse_mode=None)

mode = 0

hello_message = ("Данный бот предназначен для добавлений сообщений, медиа, текста и отправки их в разные соцсети \nЧтобы добавить файлы для отправки в такие соцсети как телеграмм, твиттер, то нужно активировать команду /social \nЧтобы добавить видео для отправки в ютуб, то нужно активировать команду /youtube \nЧтобы очистить загруженные боту сообщения, активируйте команду /remove \nПо завершению добавлению файлов нужно активировать команду /send \nПриятного использования!")

commands = [types.BotCommand('/social', 'Режим отправки для соцсетей'), 
            types.BotCommand('/youtube', 'Режим отправки для Youtube'),
            types.BotCommand('/remove', 'Очистка отправленных боту файлов из его хранилища'),
            types.BotCommand('/help', 'Мини-инструкция по пользованию ботом'),
            types.BotCommand('/send', 'Отправка сообщений в ранее выбраный режим'),
            types.BotCommand('/quit', 'Завершение работы бота')]

def send_message(mode):

    if mode == 1:
        replycator_api.send('social')
    elif mode == 2:
        replycator_api.send('youtube-social')

    return True

@bot.message_handler(commands=['social'])
def mode_soc(message):
    global mode
    if mode == 0 or mode == 2:
        mode = 1
        for filename in os.listdir("files/"):
            os.remove("files/" + filename)
        bot.reply_to(message, "Выбран режим social")
    elif mode == 1:
        bot.reply_to(message, "Данный режим уже выбран")

@bot.message_handler(commands=['start'])
def hello_user(message):   

    bot.reply_to(message, text=hello_message)

@bot.message_handler(commands=['quit'])
def quit_bot(message):   
    bot.reply_to(message, text='Выключение бота')
    sys.exit()

@bot.message_handler(commands=['help'])
def hello_user(message):

    bot.reply_to(message, text=hello_message)

@bot.message_handler(commands=['youtube'])
def mode_ytsoc(message):
    global mode
    if mode == 0 or mode == 1:
        mode = 2
        for filename in os.listdir("files/"):
            os.remove("files/" + filename)
        bot.reply_to(message, "Выбран режим youtube")
    elif mode == 2:
        bot.reply_to(message, "Данный режим уже выбран")

@bot.message_handler(commands=['remove'])
def remove_files(message):
    for filename in os.listdir("files/"):
        os.remove("files/" + filename)
    bot.reply_to(message, "Хранилище очищено")

@bot.message_handler(commands=['send'])
def send(message):
    global mode
    i = 0
    for filename in os.listdir("files/"):
        i = 1
    if i == 0:
        bot.reply_to(message, "Нечего отправлять, папка пуста")
    elif i == 1:
        bot.reply_to(message, "Идёт отправка " + str(os.listdir("files/")))
        if os.path.isfile('text.txt'):
            send_message_count = send_message(mode, file_type='all')
        else:
            send_message_count = send_message(mode)
        
        if send_message_count == True:
            bot.send_message(message, "Сообщения отправлены")
        if send_message_count == False:
            bot.send_message(message, "Сообщения не отправлены")
        
@bot.message_handler(content_types=['text'])
def text(message):
    global mode
    if mode == 0:
        bot.reply_to(message, "Не выбран режим")
    elif mode == 1:
        f = open('files/text.txt', 'a')
        f.write(f'{message.text}\n')
        print("Принят текст: " + message.text)
    elif mode == 2:
        bot.reply_to(message, "Выбран режим youtube")

@bot.message_handler(content_types=['audio'])
def audio(message):
    global mode
    if mode == 0:
        bot.reply_to(message, "Не выбран режим")
    elif mode == 1:
        fileID = message.audio.file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("files/mus"+ str(random.randint(1,999999)) +".mp3", 'wb') as new_file:
            new_file.write(downloaded_file)
            print("Принято аудио")
    elif mode == 2:
        bot.reply_to(message, "Выбран режим youtube")

@bot.message_handler(content_types=['photo'])
def photo(message):
    global mode
    if mode == 0:
        bot.reply_to(message, "Не выбран режим")
    elif mode == 1:
        fileID = message.photo[-1].file_id   
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("files/img"+ str(random.randint(1,999999)) +".jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
            print("Принято изображение")
    elif mode == 2:
        bot.reply_to(message, "Выбран режим youtube")

@bot.message_handler(content_types=['document'])
def documennt(message):
    global mode
    if mode == 0:
        bot.reply_to(message, "Не выбран режим")
    elif mode == 1:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'files/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            print("Получен документ")
    elif mode == 2:
        bot.reply_to(message, "Выбран режим youtube")

@bot.message_handler(content_types=['video'])
def video(message):
    if mode == 0:
        bot.reply_to(message, "Не выбран режим")
    elif mode == 1:
        bot.reply_to(message, "Выбран режим social")
    elif mode == 2:
        fileID = message.video.file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("files/vid"+ str(random.randint(1,999999)) +".mp4", 'wb') as new_file:
            new_file.write(downloaded_file)
            print("Принято видео")

bot.set_my_commands(commands)
bot.polling(none_stop=True)
