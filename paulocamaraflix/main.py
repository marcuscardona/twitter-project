from src.twitter_bot import twitterBot
from src.openai_prompt import openaiPrompt

def main():
    bot = twitterBot()
    prompt_generator = openaiPrompt()
    bot.tweet(text = prompt_generator.get_movie())

if __name__ == '__main__':
    main()