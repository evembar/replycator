print('Replycator Configer: Module API')

from customtkinter import *
from tkinter import PhotoImage
from replycator_modules import replycator_search_api as replysearch

if os.path.isfile('cfg/lang.py') == True:
    from cfg import lang
elif os.path.isfile('cfg/lang.py') == False:
    lang_cfg = open('cfg/lang.py', 'w')
    lang_cfg.write('lang = "en"')
    lang_cfg.close()
    from cfg import lang

twitter_status = replysearch.protect_twitter()
telegram_status = replysearch.protect_telegram()
run_rules_status = replysearch.protect_rules()

des = CTk()
des.title("Replycator API")
des.geometry("900x450")
des.resizable(False, False)

def remove_telegram_api():
    os.remove('cfg/telegram_api.py')
    delete_telegram_api.place_forget()

def remove_twitter_api():
    os.remove('cfg/tweet.client.py')
    delete_twitter_api.place_forget()

def telegram_api_editor():
    des.destroy()
    from replycator_modules import replycator_telegram_api_editor

def run_rules_editor():
    des.destroy()
    from replycator_modules import replycator_run_editor

def twitter_api_editor():
    des.destroy()
    from replycator_modules import replycator_twitter_api_editor

can = CTkCanvas(des, bg = 'black', width = 902, height = 452)
can.place(x=-1,y=-1)

background_image = PhotoImage(file='src/logo.png')
background_image_label = CTkLabel(can, image=background_image, text='')
background_image_label.place(x=10, y=10)

social_list = CTkTabview(des, fg_color='black', width=480, segmented_button_selected_color='black', segmented_button_selected_hover_color='grey', corner_radius=0)
social_list.place(x=400, y=50)

social_1 = social_list.add('1')

if lang.lang == 'en':

    twitter_api_label = CTkLabel(social_list.tab('1'), text=f'Twitter status: {twitter_status}', font=('Ubuntu', 25), bg_color='black')
    twitter_api_label.place(x=25, y=10)

    telegram_api_label = CTkLabel(social_list.tab('1'), text=f'Telegram status: {telegram_status}', font=('Ubuntu', 25), bg_color='black')
    telegram_api_label.place(x=25, y=90)

    delete_twitter_api = CTkButton(social_list.tab('1'), text='Delete Twitter API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=remove_twitter_api)
    delete_twitter_api.place(x=55, y=50)

    add_twitter_api = CTkButton(social_list.tab('1'), text='Add Twitter API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=twitter_api_editor)
    add_twitter_api.place(x=285, y=50)

    delete_telegram_api = CTkButton(social_list.tab('1'), text='Delete Telegram API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=remove_telegram_api)
    delete_telegram_api.place(x=55, y=130)

    add_telegram_api = CTkButton(social_list.tab('1'), text='Add Telegram API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=telegram_api_editor)
    add_telegram_api.place(x=285, y=130)

    edit_run_rules = CTkButton(des, text='Edit run rules', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=run_rules_editor)
    edit_run_rules.place(x=740, y=10)

if lang.lang == 'ru':

    twitter_api_label = CTkLabel(social_list.tab('1'), text=f'Twitter статус: {twitter_status}', font=('Ubuntu', 25), bg_color='black')
    twitter_api_label.place(x=25, y=10)

    telegram_api_label = CTkLabel(social_list.tab('1'), text=f'Telegram статус: {telegram_status}', font=('Ubuntu', 25), bg_color='black')
    telegram_api_label.place(x=25, y=90)

    delete_twitter_api = CTkButton(social_list.tab('1'), text='Удалить Twitter API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=remove_twitter_api)
    delete_twitter_api.place(x=55, y=50)

    add_twitter_api = CTkButton(social_list.tab('1'), text='Добав. Twitter API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=twitter_api_editor)
    add_twitter_api.place(x=285, y=50)

    delete_telegram_api = CTkButton(social_list.tab('1'), text='Удалить Telegram API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=remove_telegram_api)
    delete_telegram_api.place(x=55, y=130)

    add_telegram_api = CTkButton(social_list.tab('1'), text='Добавить Telegram API', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=telegram_api_editor)
    add_telegram_api.place(x=285, y=130)

    edit_run_rules = CTkButton(des, text='Ред. run rules', bg_color='black', border_color='white', fg_color='black', hover_color='grey', corner_radius=0, font=("Ubuntu", 20), command=run_rules_editor)
    edit_run_rules.place(x=740, y=10)

if telegram_status == 'Go to create':
    delete_telegram_api.place_forget()
elif telegram_status == 'No supported':
    delete_telegram_api.place_forget()
    add_telegram_api.place_forget()

if twitter_status == 'Go to create':
    delete_twitter_api.place_forget()
elif twitter_status == 'No supported':
    delete_twitter_api.place_forget()
    add_twitter_api.place_forget()

if run_rules_status == 'No supported':
    edit_run_rules.place_forget()

icon = PhotoImage(file='src/logo.png')
des.iconphoto(False, icon)

des.mainloop()