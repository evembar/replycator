from customtkinter import *
from cfg_sample import telegram_api_sample as telegapi
from tkinter import PhotoImage

if os.path.isfile('cfg/lang.py') == True:
    from cfg import lang
elif os.path.isfile('cfg/lang.py') == False:
    lang_cfg = open('cfg/lang.py', 'w')
    lang_cfg.write('lang = "en"')
    lang_cfg.close()
    from cfg import lang

des = CTk()
if lang.lang == 'en':
    des.title('Telegram API Editor')
if lang.lang == 'ru':
    des.title('Редактор Telegram API')
des.geometry('500x600')
des.resizable(False,False)

def write_api():
    telegapi.telegram_api = bot_api_stringvar.get()
    telegapi.telegram_channel_id = int(channel_id_intvar.get())
    telegapi.write()

can = CTkCanvas(des, bg='black', width=501, height=601)
can.place(x=-1,y=-1)

if lang.lang == 'en':

    name_editor = CTkLabel(des, bg_color='black', text='Telegram API Editor', font=("Ubuntu", 30))
    name_editor.place(x=120, y=40)

    bot_api_label = CTkLabel(des, text='Bot API', font=('Ubuntu', 20), bg_color='black')
    bot_api_label.place(x=80,y=117)

    channel_id_label = CTkLabel(des, text='Channel ID', font=('Ubuntu', 20), bg_color='black')
    channel_id_label.place(x=80,y=207)

    bot_api_stringvar = StringVar(des)
    bot_api_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 25), textvariable=bot_api_stringvar, corner_radius=0, fg_color='black', text_color='white', width=350, height=50, border_color='white', placeholder_text='client id', placeholder_text_color='white')
    bot_api_entry.place(x=80, y=150)

    channel_id_intvar = StringVar(des)
    channel_id_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 25), textvariable=channel_id_intvar, corner_radius=0, fg_color='black', text_color='white', width=350, height=50, border_color='white', placeholder_text='client id', placeholder_text_color='white')
    channel_id_entry.place(x=80, y=240)

    done_button = CTkButton(des, bg_color='white', fg_color='black', text='Done', text_color='white', corner_radius=0, font=('Ubuntu', 25), width=200, height=50, border_color='white', hover_color='grey', command=write_api)
    done_button.place(x=230, y=500)

if lang.lang == 'ru':
    name_editor = CTkLabel(des, bg_color='black', text='Редактор Telegram API', font=("Ubuntu", 30))
    name_editor.place(x=120, y=40)

    bot_api_label = CTkLabel(des, text='Bot API', font=('Ubuntu', 20), bg_color='black')
    bot_api_label.place(x=80,y=117)

    channel_id_label = CTkLabel(des, text='Channel ID', font=('Ubuntu', 20), bg_color='black')
    channel_id_label.place(x=80,y=207)

    bot_api_stringvar = StringVar(des)
    bot_api_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 25), textvariable=bot_api_stringvar, corner_radius=0, fg_color='black', text_color='white', width=350, height=50, border_color='white', placeholder_text='client id', placeholder_text_color='white')
    bot_api_entry.place(x=80, y=150)

    channel_id_intvar = StringVar(des)
    channel_id_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 25), textvariable=channel_id_intvar, corner_radius=0, fg_color='black', text_color='white', width=350, height=50, border_color='white', placeholder_text='client id', placeholder_text_color='white')
    channel_id_entry.place(x=80, y=240)

    done_button = CTkButton(des, bg_color='white', fg_color='black', text='Готово', text_color='white', corner_radius=0, font=('Ubuntu', 25), width=200, height=50, border_color='white', hover_color='grey', command=write_api)
    done_button.place(x=230, y=500)

icon = PhotoImage(file='src/logo.png')
des.iconphoto(False, icon)

des.mainloop()