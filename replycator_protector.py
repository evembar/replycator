from customtkinter import *
from replycator_modules import replycator_search_api as replysearch
from tkinter import PhotoImage
from threading import Thread

if os.path.isfile('cfg/lang.py') == True:
    from cfg import lang
elif os.path.isfile('cfg/lang.py') == False:
    lang_cfg = open('cfg/lang.py', 'w')
    lang_cfg.write('lang = "en"')
    lang_cfg.close()
    from cfg import lang

des = CTk()
des.title('Replycator protector')
des.geometry('400x250')
des.resizable(False,False)

def bot_start():
    os.system('python3 replycator_bot_aiogram.py')

bot_thread = Thread(target=bot_start)

def protector():
    if replysearch.protect_rules() == 'Go to create' or replysearch.protect_rules() == 'No supported':
        if lang.lang == 'en':
            replycator_bot_text.configure(text ='Error: not found rules')
        if lang.lang == 'ru':
            replycator_bot_text.configure(text ='Ошибка: не найдены правила')
        des.update()
        des.after(200)
        des.destroy()
        return False
    else:
        from cfg import run_rules

        if run_rules.twitter_using == True:
            if replysearch.protect_twitter() == 'Go to create' or replysearch.protect_twitter() == 'No supported':
                if lang.lang == 'en':
                    replycator_bot_text.configure(text ='Ошибка: не найден\n  twitter API файл')
                if lang.lang == 'ru':
                    replycator_bot_text.configure(text ='Ошибка: не найден\n  twitter API файл')
                des.update()
                des.after(200)
                des.destroy()
                return False
        else:
            pass

        if run_rules.telegram_using == True:
            if replysearch.protect_telegram() == 'Go to create' or replysearch.protect_telegram() == 'No supported':
                if lang.lang == 'en':
                    replycator_bot_text.configure(text ='Error: not found\n  telegram API file')
                if lang.lang == 'ru':
                    replycator_bot_text.configure(text ='Ошибка: не найден\n  telegram API файл')
                des.update()
                des.after(200)
                des.destroy()
                return False
        else:
            pass

        if lang.lang == 'en':
            replycator_bot_text.configure(text ='Done: getting start \nto Replycator bot')
        if lang.lang == 'ru':
            replycator_bot_text.configure(text ='Готово: стартуем \n Replycator бот')
        des.update()
        des.after(500)
        des.destroy()
        bot_thread.start()


reply_background = PhotoImage(file='src/logo_blur.png')

can = CTkCanvas(des, width=401, height=251, bg='black')
can.place(x=-1,y=-1)

background_label = CTkLabel(can, image=reply_background, text='')
background_label.place(x=10, y=-50)

replycator_bot_text = CTkLabel(des, text='Replycator Protector', bg_color='black', font=('Ubuntu', 25))
replycator_bot_text.place(x=78, y=20)

icon = PhotoImage(file='src/logo.png')
des.iconphoto(False, icon)

des.after(500, protector)

des.mainloop()