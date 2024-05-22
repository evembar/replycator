print("Replycator API 0.01")

import os
from replycator_modules import replycator_twitter_sender as replytweet

def delete_files():
    for filename in os.listdir("files/"):
        os.remove("files/" + filename)

def send(mode, file_type=None):

    if mode == 'twitter':

        if file_type == 'all':
            replytweet.send(with_text=True)
        else:
            replytweet.send()
