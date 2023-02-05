import os
import datetime
import tweepy
from dotenv import load_dotenv

load_dotenv()

class twitterBot:
    '''
    Main class for a general Twitter bot using Tweepy
    
    Authors: 
        @joaoreboucas1

    Since:
        02-2023.
    '''

    def __init__(self):
        '''
        Initializes an API client that authorizes our connection with Twitter.
        Also updates the last connection
        '''
        self.client = tweepy.Client(consumer_key=os.getenv('TWEEPY_CONSUMER_KEY')
                     , consumer_secret=os.getenv('TWEEPY_CONSUMER_SECRET')
                     , bearer_token=os.getenv('TWEEPY_BEARER_TOKEN')
                     , access_token=os.getenv('TWEEPY_ACCESS_TOKEN')
                     , access_token_secret=os.getenv('TWEEPY_ACCESS_TOKEN_SECRET')
                     , wait_on_rate_limit=True)
        self.last_connection = datetime.datetime.now()

    def tweet(self, text):
        self.client.create_tweet(text=text)

    def send_dm(self, recipient_username, text):
        recipient_data = self.client.get_user(username=recipient_username)
        recipient_id = recipient_data.data.data['id']
        self.client.create_direct_message(participant_id=recipient_id, text=text)

