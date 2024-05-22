import os

twitter_using = ''
telegram_using = ''

if os.path.isfile('cfg/run_rules.py') == True:
    run_rules_reality = True
elif os.path.isfile('cfg/run_rules.py') == False:
    run_rules_reality = False

def write():
    if run_rules_reality == False:
        run_rules_file = open('cfg/run_rules.py', 'w')
        run_rules_file.write(f'twitter_using = {twitter_using}\ntelegram_using = {telegram_using}')
        run_rules_file.close()
        return True
    elif run_rules_reality == True:
        os.remove('cfg/run_rules.py')
        run_rules_file = open('cfg/run_rules.py', 'w')
        run_rules_file.write(f'twitter_using = {twitter_using}\ntelegram_using = {telegram_using}')
        run_rules_file.close()
        return True
    else:
        return False