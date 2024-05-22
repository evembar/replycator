from customtkinter import *
from cfg_sample import run_rules_sample as rusam
from tkinter import PhotoImage

des = CTk()
des.title('Run Rules Editor')
des.geometry('300x400')
des.resizable(False,False)

can = CTkCanvas(des, bg='black', width=301, height=401)
can.place(x=-1,y=-1)

name_editor = CTkLabel(des, bg_color='black', text='Run Rules Editor', font=("Ubuntu", 26))
name_editor.place(x=50, y=20)

def telegram_using_switch_event():
    telegram_using_switch.configure(text=f"Telegram using: {telegram_using_switch_var.get()}")
    des.update()

def twitter_using_switch_event():
    twitter_using_switch.configure(text=f"Twitter using: {twitter_using_switch_var.get()}")
    des.update()

def rusam_write():
    if telegram_using_switch_var.get() == "False":
        rusam.telegram_using = False
    elif telegram_using_switch_var.get() == "True":
        rusam.telegram_using = True

    if twitter_using_switch_var.get()== "False":
        rusam.twitter_using = False
    elif twitter_using_switch_var.get() == "True":
        rusam.twitter_using = True

    rusam.write()

telegram_using_switch_var = StringVar(value="True")
telegram_using_switch = CTkSwitch(des, text=f"Telegram using: {telegram_using_switch_var.get()}", font=('Ubuntu',20), command=telegram_using_switch_event,
                                 variable=telegram_using_switch_var, onvalue="True", offvalue="False", bg_color='black', progress_color='white', button_color='grey', button_hover_color='black')
telegram_using_switch.place(x=20, y=80)

twitter_using_switch_var = StringVar(value="True")
twitter_using_switch = CTkSwitch(des, text=f"Twitter using: {telegram_using_switch_var.get()}", font=('Ubuntu',20), command=twitter_using_switch_event,
                                 variable=twitter_using_switch_var, onvalue="True", offvalue="False", bg_color='black', progress_color='white', button_color='grey', button_hover_color='black')
twitter_using_switch.place(x=20, y=120)

done_button = CTkButton(des, bg_color='white', fg_color='black', text='Done', text_color='white', corner_radius=0, font=('Ubuntu', 25), width=300, height=50, border_color='white', hover_color='grey', command=rusam_write)
done_button.place(x=0, y=340)

icon = PhotoImage(file='src/logo.png')
des.iconphoto(False, icon)

des.mainloop()