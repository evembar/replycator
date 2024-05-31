from customtkinter import *
from cfg_sample import twitter_api_sample as twitapi
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
    des.title('Twitter API Editor')
if lang.lang == 'ru':
    des.title('Редактор Twitter API')

des.geometry('500x600')
des.resizable(False,False)

def write_api():
    twitapi.twitter_api = [consumer_key_stringvar.get(),consumer_secret_stringvar.get(), access_key_stringvar.get(),access_token_secret_stringvar.get()]
    twitapi.write()

can = CTkCanvas(des, bg='black', width=501, height=601)
can.place(x=-1,y=-1)

if lang.lang == 'en':

    name_editor = CTkLabel(des, bg_color='black', text='Twitter API Editor', font=("Ubuntu", 30))
    name_editor.place(x=120, y=40)

    consumer_key_label = CTkLabel(des, text='API key', font=('Ubuntu', 20), bg_color='black')
    consumer_key_label.place(x=80,y=95)

    consumer_secret_label = CTkLabel(des, text='API secret', font=('Ubuntu', 20), bg_color='black')
    consumer_secret_label.place(x=80,y=165)

    access_key_label = CTkLabel(des, text='Access token', font=('Ubuntu', 20), bg_color='black')
    access_key_label.place(x=80,y=235)

    access_token_secret_label = CTkLabel(des, text='Access token secret', font=('Ubuntu', 20), bg_color='black')
    access_token_secret_label.place(x=80,y=305)

if lang.lang == 'ru':
    
    name_editor = CTkLabel(des, bg_color='black', text='Редактор Twitter API', font=("Ubuntu", 30))
    name_editor.place(x=120, y=40)

    consumer_key_label = CTkLabel(des, text='API key', font=('Ubuntu', 20), bg_color='black')
    consumer_key_label.place(x=80,y=95)

    consumer_secret_label = CTkLabel(des, text='API secret', font=('Ubuntu', 20), bg_color='black')
    consumer_secret_label.place(x=80,y=165)

    access_key_label = CTkLabel(des, text='Access token', font=('Ubuntu', 20), bg_color='black')
    access_key_label.place(x=80,y=235)

    access_token_secret_label = CTkLabel(des, text='Access token secret', font=('Ubuntu', 20), bg_color='black')
    access_token_secret_label.place(x=80,y=305)


consumer_key_stringvar = StringVar(des)
consumer_key_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 22), textvariable=consumer_key_stringvar, corner_radius=0, fg_color='black', text_color='white', width=350, border_color='white', placeholder_text='client id', placeholder_text_color='white')
consumer_key_entry.place(x=80, y=125)

consumer_secret_stringvar = StringVar(des)
consumer_secret_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 22), textvariable=consumer_secret_stringvar, corner_radius=0, fg_color='black', text_color='white', width=350, border_color='white', placeholder_text='client id', placeholder_text_color='white')
consumer_secret_entry.place(x=80, y=195)

access_key_stringvar = StringVar(des)
access_key_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 22), textvariable=access_key_stringvar, corner_radius=0, fg_color='black', text_color='white', width=350, border_color='white', placeholder_text='client id', placeholder_text_color='white')
access_key_entry.place(x=80, y=265)

access_token_secret_stringvar = StringVar(des)
access_token_secret_entry = CTkEntry(des, bg_color='black', font=('Ubuntu', 22), textvariable=access_token_secret_stringvar, corner_radius=0, fg_color='black', text_color='white', width=350, border_color='white', placeholder_text='client id', placeholder_text_color='white')
access_token_secret_entry.place(x=80, y=335)

if lang.lang == 'en':
    done_button = CTkButton(des, bg_color='white', fg_color='black', text='Done', text_color='white', corner_radius=0, font=('Ubuntu', 25), width=200, height=50, border_color='white', hover_color='grey', command=write_api)
    done_button.place(x=230, y=500)
if lang.lang == 'ru':
    done_button = CTkButton(des, bg_color='white', fg_color='black', text='Готово', text_color='white', corner_radius=0, font=('Ubuntu', 25), width=200, height=50, border_color='white', hover_color='grey', command=write_api)
    done_button.place(x=230, y=500)

icon = PhotoImage(file='src/logo.png')
des.iconphoto(False, icon)

des.mainloop()