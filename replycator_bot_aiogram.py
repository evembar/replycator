print('Replycator BOT 1.00')

import random, os, sys, replycator_api, asyncio
from aiogram import *
from cfg import telegram_api as tgapi
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cfg import run_rules

if os.path.isfile('cfg/lang.py') == True:
    from cfg import lang
elif os.path.isfile('cfg/lang.py') == False:
    lang_cfg = open('cfg/lang.py', 'w')
    lang_cfg.write('lang = "en"')
    lang_cfg.close()
    from cfg import lang

bot_api = tgapi.telegram_api

bot = Bot(token=bot_api, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

mode = 0

if lang.lang == 'en':

    hello_message = ("This bot is designed to add messages, media, text and send them to different social networks. \nTo add files to send to such social networks as telegram, Twitter, then you need to activate the /social\nIf command to clear the messages uploaded to the bot, activate the command /remove \n Upon completion of adding files, you need to activate the /send \n command for pleasant use!")

    commands = [types.BotCommand('/social', 'Sending mode for social networks'), 
                types.BotCommand('/remove', 'Clearing files sent to the bot from its storage'),
                types.BotCommand('/help', 'Mini-instructions for using the bot'),
                types.BotCommand('/send', 'Sending messages to the previously selected mode'),
                types.BotCommand('/quit', 'Shutting down the bot')]

    async def telegram_send():
        for filename in os.listdir("files/"):
            #os.remove("files/" + filename)

            extension = filename.split('.')[-1]
            print(extension)
            if extension == 'mp3' or extension == 'ogg' or extension == 'wav':
                with open(f'files/{filename}', 'rb') as music:
                    await bot.send_audio(tgapi.telegram_channel_id, music)
                    music.close()
            elif extension == 'png' or extension == 'jpg' or extension == 'webp' or extension == 'bmp':
                with open(f'files/{filename}', 'rb') as photo:
                    await bot.send_photo(tgapi.telegram_channel_id, photo)
                    photo.close()
            elif extension == 'webm' or extension == 'mkv' or extension == 'mp4':
                with open(f'files/{filename}', 'rb') as video:
                    await bot.send_video(tgapi.telegram_channel_id, video)
                    video.close()
            elif extension == 'txt':
                with open(f'files/{filename}', 'r') as text:
                    text_var = text.read()
                    await bot.send_message(tgapi.telegram_channel_id, text_var)
                    text.close()
            else:
                with open(f'files/{filename}', 'rb') as file:
                    await bot.send_document(tgapi.telegram_channel_id, file)
                    file.close()

    async def send_message(mode=1):


        if run_rules.telegram_using == True:
            await telegram_send()
        elif run_rules.telegram_using == False:
            pass

        if run_rules.twitter_using == True:
            replycator_api.send('twitter')
        elif run_rules.twitter_using == False:
            pass
        
        return True

    @dp.message_handler(commands=['social'])
    async def mode_soc(message:types.Message):
        global mode
        if mode == 0 or mode == 2:
            mode = 1
            for filename in os.listdir("files/"):
                os.remove("files/" + filename)
            await message.reply("The social mode is selected")
        elif mode == 1:
            await message.reply("This mode has already been selected")

    @dp.message_handler(commands=['start'])
    async def hello_user(message: types.Message):   
        await message.reply(message, text=hello_message)

    @dp.message_handler(commands=['quit'])
    async def quit_bot(message: types.Message):   
        await message.reply(text='Turning off the bot')
        sys.exit()

    @dp.message_handler(commands=['help'])
    async def hello_user(message: types.Message):
        await message.reply(text=hello_message)

    @dp.message_handler(commands=['remove'])
    async def remove_files(message: types.Message):
        for filename in os.listdir("files/"):
            os.remove("files/" + filename)
        await message.reply("The storage has been cleared")

    @dp.message_handler(commands=['send'])
    async def send(message: types.Message):
        global mode
        i = 0
        for filename in os.listdir("files/"):
            i = 1
        if i == 0:
            await message.reply("There is nothing to send, the folder is empty")
        elif i == 1:
            await message.reply("Sending is underway " + str(os.listdir("files/")))
            send_message_count = await send_message(mode)
            
            if send_message_count == True:
                replycator_api.delete_files()
                await message.answer("Messages have been sent")
            if send_message_count == False:
                replycator_api.delete_files()
                await message.answer("Messages have not been sent")
            
    @dp.message_handler(content_types=['text'])
    async def text(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("The mode is not selected")
        elif mode == 1:
            f = open('files/text.txt', 'a')
            f.write(f'{message.text}\n')
            print("The text has been accepted: " + message.text)

    @dp.message_handler(content_types=['audio'])
    async def audio(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("The mode is not selected")
        elif mode == 1:
            fileID = message.audio.file_id
            file_info = await bot.get_file(fileID)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open("files/mus"+ str(random.randint(1,999999)) +".mp3", 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("Audio received")

    @dp.message_handler(content_types=['photo'])
    async def photo(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("The mode is not selected")
        elif mode == 1:
            fileID = message.photo[-1].file_id   
            file_info = await bot.get_file(fileID)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open("files/img"+ str(random.randint(1,999999)) +".jpg", 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("The image is accepted")

    @dp.message_handler(content_types=['document'])
    async def documennt(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("The mode is not selected")
        elif mode == 1:
            file_info = await bot.get_file(message.document.file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = 'files/' + message.document.file_name;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("Document received")

    @dp.message_handler(content_types=['video'])
    async def video(message: types.Message):
        if mode == 0:
            await message.reply("The mode is not selected")
        elif mode == 1:
            fileID = message.video.file_id
            file_info = await bot.get_file(fileID)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open("files/vid"+ str(random.randint(1,999999)) +".mp4", 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("Video accepted")

if lang.lang == 'ru':

    hello_message = ("Данный бот предназначен для добавлений сообщений, медиа, текста и отправки их в разные соцсети \nЧтобы добавить файлы для отправки в такие соцсети как телеграмм, твиттер, то нужно активировать команду /social\nЧтобы очистить загруженные боту сообщения, активируйте команду /remove \nПо завершению добавлению файлов нужно активировать команду /send \nПриятного использования!")

    commands = [types.BotCommand('/social', 'Режим отправки для соцсетей'), 
                types.BotCommand('/remove', 'Очистка отправленных боту файлов из его хранилища'),
                types.BotCommand('/help', 'Мини-инструкция по пользованию ботом'),
                types.BotCommand('/send', 'Отправка сообщений в ранее выбраный режим'),
                types.BotCommand('/quit', 'Завершение работы бота')]

    async def telegram_send():
        for filename in os.listdir("files/"):
            #os.remove("files/" + filename)

            extension = filename.split('.')[-1]
            print(extension)
            if extension == 'mp3' or extension == 'ogg' or extension == 'wav':
                with open(f'files/{filename}', 'rb') as music:
                    await bot.send_audio(tgapi.telegram_channel_id, music)
                    music.close()
            elif extension == 'png' or extension == 'jpg' or extension == 'webp' or extension == 'bmp':
                with open(f'files/{filename}', 'rb') as photo:
                    await bot.send_photo(tgapi.telegram_channel_id, photo)
                    photo.close()
            elif extension == 'webm' or extension == 'mkv' or extension == 'mp4':
                with open(f'files/{filename}', 'rb') as video:
                    await bot.send_video(tgapi.telegram_channel_id, video)
                    video.close()
            elif extension == 'txt':
                with open(f'files/{filename}', 'r') as text:
                    text_var = text.read()
                    await bot.send_message(tgapi.telegram_channel_id, text_var)
                    text.close()
            else:
                with open(f'files/{filename}', 'rb') as file:
                    await bot.send_document(tgapi.telegram_channel_id, file)
                    file.close()

    async def send_message(mode=1):


        if run_rules.telegram_using == True:
            await telegram_send()
        elif run_rules.telegram_using == False:
            pass

        if run_rules.twitter_using == True:
            replycator_api.send('twitter')
        elif run_rules.twitter_using == False:
            pass
        
        return True

    @dp.message_handler(commands=['social'])
    async def mode_soc(message:types.Message):
        global mode
        if mode == 0 or mode == 2:
            mode = 1
            for filename in os.listdir("files/"):
                os.remove("files/" + filename)
            await message.reply("Выбран режим social")
        elif mode == 1:
            await message.reply("Данный режим уже выбран")

    @dp.message_handler(commands=['start'])
    async def hello_user(message: types.Message):   
        await message.reply(message, text=hello_message)

    @dp.message_handler(commands=['quit'])
    async def quit_bot(message: types.Message):   
        await message.reply(text='Выключение бота')
        sys.exit()

    @dp.message_handler(commands=['help'])
    async def hello_user(message: types.Message):
        await message.reply(text=hello_message)

    @dp.message_handler(commands=['remove'])
    async def remove_files(message: types.Message):
        for filename in os.listdir("files/"):
            os.remove("files/" + filename)
        await message.reply("Хранилище очищено")

    @dp.message_handler(commands=['send'])
    async def send(message: types.Message):
        global mode
        i = 0
        for filename in os.listdir("files/"):
            i = 1
        if i == 0:
            await message.reply("Нечего отправлять, папка пуста")
        elif i == 1:
            await message.reply("Идёт отправка " + str(os.listdir("files/")))
            send_message_count = await send_message(mode)
            
            if send_message_count == True:
                replycator_api.delete_files()
                await message.answer("Сообщения отправлены")
            if send_message_count == False:
                replycator_api.delete_files()
                await message.answer("Сообщения не отправлены")
            
    @dp.message_handler(content_types=['text'])
    async def text(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("Не выбран режим")
        elif mode == 1:
            f = open('files/text.txt', 'a')
            f.write(f'{message.text}\n')
            print("Принят текст: " + message.text)

    @dp.message_handler(content_types=['audio'])
    async def audio(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("Не выбран режим")
        elif mode == 1:
            fileID = message.audio.file_id
            file_info = await bot.get_file(fileID)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open("files/mus"+ str(random.randint(1,999999)) +".mp3", 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("Принято аудио")

    @dp.message_handler(content_types=['photo'])
    async def photo(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("Не выбран режим")
        elif mode == 1:
            fileID = message.photo[-1].file_id   
            file_info = await bot.get_file(fileID)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open("files/img"+ str(random.randint(1,999999)) +".jpg", 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("Принято изображение")

    @dp.message_handler(content_types=['document'])
    async def documennt(message: types.Message):
        global mode
        if mode == 0:
            await message.reply("Не выбран режим")
        elif mode == 1:
            file_info = await bot.get_file(message.document.file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = 'files/' + message.document.file_name;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("Получен документ")

    @dp.message_handler(content_types=['video'])
    async def video(message: types.Message):
        if mode == 0:
            await message.reply("Не выбран режим")
        elif mode == 1:
            fileID = message.video.file_id
            file_info = await bot.get_file(fileID)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open("files/vid"+ str(random.randint(1,999999)) +".mp4", 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
                print("Принято видео")

async def commands_replycator(_):
    await bot.set_my_commands(commands)

executor.start_polling(dp, skip_updates=True, on_startup=commands_replycator)
