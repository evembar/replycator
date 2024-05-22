import os

def protect_twitter():
    if os.path.isfile('cfg_sample/twitter_api_sample.py'):
        if os.path.isfile('cfg/tweet.py') == False:
            return 'Go to create'
        elif os.path.isfile('cfg/tweet.py') == True:
            return True
        elif os.path.isfile('cfg_sample/twitter_api_sample.py') == False:
            return 'No supported'     

def protect_telegram():
    if os.path.isfile('cfg_sample/telegram_api_sample.py') == True:
        if os.path.isfile('cfg/telegram_api.py') == False:
            return 'Go to create'
        elif os.path.isfile('cfg/telegram_api.py') == True:
            return True
    elif os.path.isfile('cfg_sample/telegram_api_sample.py') == False:
        return 'No supported'
    
def protect_rules():
    if os.path.isfile('cfg_sample/run_rules_sample.py') == True:
        if os.path.isfile('cfg/run_rules.py') == False:
            return 'Go to create'
        elif os.path.isfile('cfg/run_rules.py') == True:
            return True
    elif os.path.isfile('cfg_sample/run_rules_sample.py') == False:
        return 'No supported'