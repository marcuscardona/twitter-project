from src.twitter_bot import twitterBot
from src.openai_prompt import openaiPrompt
from src.sql_connector import sqlConnector
from dotenv import load_dotenv
from datetime import datetime
import os

def main():
    
    load_dotenv()
    bot = twitterBot()
    prompt_generator = openaiPrompt()
    
    # Get the movie params output
    movies_params = prompt_generator.get_movie()
    movie = movies_params['generated_movie']
    
    tweet_id = bot.tweet(text = movie)
    
    # Store the data in DB
    #schema ={
    #    'date': datetime.now().date()
    #  , 'first_tweet_id': tweet_id
    #  , 'genres': movies_params['genres']
    #  , 'protagonist_name': movies_params['protagonist_name']
    #  , 'protagonist_surname': movies_params['protagonist_surname']
    #  , 'occupations': movies_params['occupations']
    #  , 'occupation_complements': movies_params['occupation_complements']
    #  , 'adjectives': movies_params['adjectives']
    #  , 'first_famous_people': movies_params['first_famous_people']
    #  , 'second_famous_people': movies_params['second_famous_people']
    #  , 'first_theme': movies_params['first_theme']
    #  , 'second_theme': movies_params['second_theme']
    #  , 'generated_movie': str(movies_params['generated_movie'])
    #}
#
    #sql = sqlConnector(username=os.getenv('SQL_USER')
    #              , password=os.getenv('SQL_PASSWORD')
    #              , server=os.getenv('SQL_SERVER')
    #              , port=os.getenv('SQL_PORT')
    #              , database='tp')
#
    #sql.insertInto('paulocamaraflix', schema)

if __name__ == '__main__':
    main()