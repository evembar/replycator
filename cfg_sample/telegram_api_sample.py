import os

telegram_api = ''
telegram_channel_id = ''

if os.path.isfile('cfg/telegram_api.py') == True:
    telegram_api_reality = True
elif os.path.isfile('cfg/telegram_api.py') == False:
    telegram_api_reality = False

def write():
    if telegram_api_reality == False:
        telegram_api_file = open('cfg/telegram_api.py', 'w')
        telegram_api_file.write(f'telegram_api = "{telegram_api}"\ntelegram_channel_id = {telegram_channel_id}')
        telegram_api_file.close()
        return True
    elif telegram_api_reality == True:
        os.remove('cfg/telegram_api.py')
        telegram_api_file = open('cfg/telegram_api.py', 'w')
        telegram_api_file.write(f'telegram_api = {telegram_api}\ntelegram_channel_id = {telegram_channel_id}')
        telegram_api_file.close()
        return True
    else:
        return False