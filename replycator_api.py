print("Replycator API 1.00")

import os
from replycator_modules import replycator_twitter_sender as replytweet

if os.path.isdir('files') == True:
    pass
elif os.path.isdir('files') == False:
    os.mkdir('files')

def delete_files():
    for filename in os.listdir("files/"):
        os.remove("files/" + filename)

def send(mode, file_type=None):

    if mode == 'twitter':

        if file_type == 'all':
            replytweet.send(with_text=True)
        else:
            replytweet.send()
