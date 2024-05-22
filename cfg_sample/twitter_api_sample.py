import os

twitter_api = []

if os.path.isfile('cfg/tweet.py') == True:
    telegram_api_reality = True
elif os.path.isfile('cfg/tweet.py') == False:
    telegram_api_reality = False

def write():
    if telegram_api_reality == False:
        twitter_api_file = open('cfg/tweet.py', 'w')
        twitter_api_file.write(f'API_KEY="{twitter_api[0]}"\nAPI_SECRET="{twitter_api[1]}"\nACCESS_TOKEN="{twitter_api[2]}"\nACCESS_TOKEN_SECRET="{twitter_api[3]}"')
        return False
    elif telegram_api_reality == True:
        os.remove('cfg/tweet.py')
        twitter_api_file = open('cfg/tweet.py', 'w')
        twitter_api_file.write(f'API_KEY="{twitter_api[0]}"\nAPI_SECRET="{twitter_api[1]}"\nACCESS_TOKEN="{twitter_api[2]}"\nACCESS_TOKEN_SECRET="{twitter_api[3]}"')
        return True
    else:
        return False