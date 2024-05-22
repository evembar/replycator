import pyglet
import os
from threading import Thread

def bot_start():
    os.system('python3 replycator_protector.py')
        
def about_replycator():
    os.system('python3 replycator_configer_about.py')
def replycator_api():
    os.system('python3 replycator_configer_api.py')

number_version = 0.01
button_name_active = None
print(f'Replycator Configer {number_version}')

icon = pyglet.image.load('src/icon.ico')

des = pyglet.window.Window()
des.set_caption(f'Replycator {number_version}')
des.set_size(1000,500)
des.set_icon(icon)

batch = pyglet.graphics.Batch()

background_image = pyglet.resource.image('src/logo.png')
btn_image = [pyglet.image.load('src/btn.png'),
             pyglet.image.load('src/btn_1.png')]

welcome_text = pyglet.text.Label(text=f'Welcome to Replycator {number_version}', font_name='Ubuntu Light', font_size=20, x=498, y=425)
btn_enable_bot = pyglet.sprite.Sprite(img=btn_image[0], x=530, y=280, batch=batch)
btn_enable_bot_text = pyglet.text.Label(text=' Enable bot', font_name='Ubuntu', font_size=15, x=540, y=305)

btn_about_replycator = pyglet.sprite.Sprite(img=btn_image[0], x=690, y=280, batch=batch)
btn_about_replycator_text = pyglet.text.Label(text='    About', font_name='Ubuntu', font_size=17, x=700, y=305)

btn_api = pyglet.sprite.Sprite(img=btn_image[0], x=610, y=180, batch=batch)
btn_api_text = pyglet.text.Label(text='   API', font_name='Ubuntu', font_size=25, x=623, y=204)

warning_bot_text = pyglet.text.Label(text='', font_name='Ubuntu', font_size=14, x=615, y=375)

@des.event
def on_draw():
    des.clear()
    background_image.blit(0,70)
    btn_enable_bot.draw()
    btn_enable_bot_text.draw()
    btn_about_replycator.draw()
    btn_about_replycator_text.draw()
    btn_api.draw()
    btn_api_text.draw()
    welcome_text.draw()
    warning_bot_text.draw()

@des.event
def on_mouse_press(x, y, button, modifiers):
    if button == 1:
        if button_name_active == 'about_replycator':
            print("about")
            btn_about_replycator.image = btn_image[0]
            warning_bot_text.text = 'About Replycator'
            bot_starter = Thread(target=about_replycator)
            bot_starter.start()   
        elif button_name_active == 'api':
            print('api')
            btn_api.image = btn_image[0]
            warning_bot_text.text = 'Active configurator'
            bot_starter = Thread(target=replycator_api)
            bot_starter.start()  
        elif button_name_active == 'enable_bot':
            print('enable_bot')
            btn_enable_bot.image = btn_image[0]
            warning_bot_text.text = 'Activate bot'
            bot_starter = Thread(target=bot_start)
            bot_starter.start()   
                
@des.event
def on_mouse_motion(x, y, dx, dy):
    global button_name_active
    if x>btn_about_replycator.x and x< btn_about_replycator.x+128 and y>btn_about_replycator.y and y<btn_about_replycator.y+64:
        button_name_active = 'about_replycator'
        btn_about_replycator.image = btn_image[1]        
    elif x>btn_api.x and x< btn_api.x+128 and y>btn_api.y and y<btn_api.y+64:
        button_name_active = 'api'
        btn_api.image = btn_image[1]   
    elif x>btn_enable_bot.x and x< btn_enable_bot.x+128 and y>btn_enable_bot.y and y<btn_enable_bot.y+64:
        button_name_active = 'enable_bot'
        btn_enable_bot.image = btn_image[1]   
    else:
        button_name_active = None
        btn_about_replycator.image = btn_image[0]
        btn_enable_bot.image = btn_image[0]
        btn_api.image = btn_image[0]   

pyglet.app.run()
