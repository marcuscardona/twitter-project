import os
import datetime
import tweepy
from dotenv import load_dotenv
import time

load_dotenv()

class twitterBot():
  
    def __init__(self):
        """
        Initializes an API client that authorizes our connection with Twitter.
        Also updates the last connection.

        The API Keys are stored in a .env file.

        Authors:
            @joaoreboucas1
            @marcuscardona

        Since:
            02-2023
        """
        self.client = tweepy.Client(consumer_key=os.getenv('TWEEPY_CONSUMER_KEY_PCF')
                     , consumer_secret=os.getenv('TWEEPY_CONSUMER_SECRET_PCF')
                     , bearer_token=os.getenv('TWEEPY_BEARER_TOKEN_PCF')
                     , access_token=os.getenv('TWEEPY_ACCESS_TOKEN_PCF')
                     , access_token_secret=os.getenv('TWEEPY_ACCESS_TOKEN_SECRET_PCF')
                     , wait_on_rate_limit=True)
        self.last_connection = datetime.datetime.now()

    def turn_long_text_into_tweets(self, long_text):
        """
        Separates a long string into a list of strings whose length is less than 280.

        Inputs:
            long_text = string text

        Outputs:
            List of strings of lenght less than 280.
        Authors:
            @joaoreboucas1
        
        Since:
            02-2023.
        """
        words = long_text.split(' ')
        tweets = ['']
        number_of_tweets = 1
        for word in words:
            length = len(tweets[number_of_tweets-1])
            if length < 280-len(word):
                tweets[number_of_tweets-1] += word+' '
            else:
                tweets.append('')
                number_of_tweets += 1
                tweets[number_of_tweets-1] += word+' '
        return tweets

    def tweet(self, text):
        """
        Tweets a string of text. If the length of text 280, a thread is created using the 
        long_text_into_tweets function.

        Inputs:
            text = string of text

        Outputs:
            A tweet from the username logged into the bot.

        Authors:
            @joaoreboucas1
            @marcuscardona
        
        Since:
            02-2023.
        """
        
        if len(text) > 280:
            list_text = self.turn_long_text_into_tweets(text)
            for i, tweets in enumerate(list_text):
                if i == 0:
                    last_tweet_id = self.client.create_tweet(text=tweets).data['id']
                    time.sleep(10)
                else:
                    last_tweet_id = self.client.create_tweet(text=tweets
                                                           , in_reply_to_tweet_id = last_tweet_id).data['id']
                    time.sleep(10)
        else:
            self.client.create_tweet(text=text)
    

    def send_dm(self, recipient_username, text):
        recipient_data = self.client.get_user(username=recipient_username)
        recipient_id = recipient_data.data.data['id']
        self.client.create_direct_message(participant_id=recipient_id, text=text)

