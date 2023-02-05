from ... import classes.twitter_bot.twitterBot

from ... import classes.openai_prompt.openaiPrompt

def main():
    bot = twitterBot
    prompt_generator = openaiPrompt()
    bot.tweet(prompt_generator.get_movie())

if __name__ == '__main__':
    main()
