import pyglet
import os
from pyglet import shapes

if os.path.isfile('cfg/lang.py') == True:
    from cfg import lang
elif os.path.isfile('cfg/lang.py') == False:
    lang_cfg = open('cfg/lang.py', 'w')
    lang_cfg.write('lang = "en"')
    lang_cfg.close()
    from cfg import lang

print("Replycator Configer: About Module ")

icon = pyglet.image.load('src/icon.ico')
ver = 1.00

des = pyglet.window.Window()
if lang.lang == 'en':
    des.set_caption("About Replycator")
if lang.lang == 'ru':
    des.set_caption("О Replycator")
des.set_size(width = 360, height = 500)
des.set_icon(icon)

batch = pyglet.graphics.Batch()

ani = pyglet.resource.animation('src/backround_about.gif')
background_image = pyglet.sprite.Sprite(img=ani, x=0,y=-35)

square = shapes.Rectangle(40, -20, 280, 150, color=(10, 10, 10), batch=batch)

source = pyglet.media.load(filename='src/replycator.ogg')
player = pyglet.media.Player()
player.loop = True
player.queue(source)
player.play()

if lang.lang == 'en':
    replycator_text = pyglet.text.Label(text=f'Replycator {ver}', font_name='Ubuntu', font_size=15, align='center',width=360, x=0, y=98)
    developer_configer = pyglet.text.Label(text=f'Developer configer by WebMast', font_name='Ubuntu', font_size=13, align='center',width=360, x=0, y=68)
    developer_telegram_bot = pyglet.text.Label(text=f'Developer telegram bot by Nikita44', font_name='Ubuntu', font_size=13, align='center',width=360, x=0, y=48)
    designer_configer = pyglet.text.Label(text=f'Design configer by Ikso', font_name='Ubuntu', font_size=13, align='center',width=360, x=0, y=28)
    walm2024 = pyglet.text.Label(text=f'WALM 2024', font_name='Ubuntu', font_size=15, align='center',width=360, x=0, y=4)
if lang.lang == 'ru':
    replycator_text = pyglet.text.Label(text=f'Replycator {ver}', font_name='Ubuntu', font_size=15, align='center',width=360, x=0, y=98)
    developer_configer = pyglet.text.Label(text=f'Разраб конфигера - WebMast', font_name='Ubuntu', font_size=13, align='center',width=360, x=0, y=68)
    developer_telegram_bot = pyglet.text.Label(text=f'Разраб тг бота - Nikita44', font_name='Ubuntu', font_size=13, align='center',width=360, x=0, y=48)
    designer_configer = pyglet.text.Label(text=f'Дизайн конфигера -  Ikso', font_name='Ubuntu', font_size=13, align='center',width=360, x=0, y=28)
    walm2024 = pyglet.text.Label(text=f'WALM 2024', font_name='Ubuntu', font_size=15, align='center',width=360, x=0, y=4)

@des.event()
def on_draw():
    des.clear()

    background_image.draw()
    square.draw()
    replycator_text.draw()
    developer_configer.draw()
    developer_telegram_bot.draw()
    designer_configer.draw()
    walm2024.draw()

pyglet.app.run()

