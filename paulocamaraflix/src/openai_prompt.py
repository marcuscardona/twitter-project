from dotenv import load_dotenv
import os
from pathlib import Path
import random
import openai
from . import tp_logger

class openaiPrompt():

    def __init__(self):
        load_dotenv()
        self._api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self._api_key
        self._logger = tp_logger.logConstructor(file_name='openAI').createLogger()

    def read_prompt(self, filename):
        """
        Looks in `prompts/` directory for a text file. Pass in file name only, not extension.
        Example: `prompts/hello-world.txt` -> read_prompt('hello-world')

        Authors:
            @OthersideAI
        """
        
        return Path('./prompts/{0}.txt'.format(filename)).read_text(encoding='UTF-8')

    def get_movie(self):
        """
        Returns a Davinci-003 prompt generated from the movie_script.txt

        Authors:
            @marcuscardona
        
        Since:
            02-2023
        """
        # Load the movie_script prompt
        movie_prompt = self.read_prompt('movie_script')
        
        # Random choice from the parameters on movie_script
        genres=random.choice(self.read_prompt('genres').split('\n'))
        protagonist_name=random.choice(self.read_prompt('protagonist_name').split('\n'))
        protagonist_surname=random.choice(self.read_prompt('protagonist_surname').split('\n'))
        occupations=random.choice(self.read_prompt('occupations').split('\n'))
        occupation_complements=random.choice(self.read_prompt('occupation_complements').split('\n'))          
        adjectives=random.choice(self.read_prompt('adjectives').split('\n'))
        first_famous_people=random.choice(self.read_prompt('famous_people').split('\n'))
        second_famous_people=random.choice(self.read_prompt('famous_people').split('\n'))
        first_theme=random.choice(self.read_prompt('themes').split('\n'))
        second_theme=random.choice(self.read_prompt('themes').split('\n'))
        
        # Format Query
        query = movie_prompt.format(
            genres
          , protagonist_name
          , protagonist_surname
          , occupations
          , occupation_complements
          , adjectives
          , first_famous_people
          , second_famous_people
          , first_theme
          , second_theme
        )

        # Create Generated Text
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            temperature=0.6,
            max_tokens = 1000
        )

        # Get the text from the json response
        generated_movie=response.choices[0].text
        
        self._logger.info(f'{response.usage.prompt_tokens} prompt + {response.usage.completion_tokens} completion = {response.usage.total_tokens} tokens')
             
        # Transform the parameters in list
        output = {
          'genres':genres
        , 'protagonist_name':protagonist_name
        , 'protagonist_surname':protagonist_surname
        , 'occupations':occupations
        , 'occupation_complements':occupation_complements
        , 'adjectives':adjectives
        , 'first_famous_people':first_famous_people
        , 'second_famous_people':second_famous_people
        , 'first_theme':first_theme
        , 'second_theme':second_theme
        , 'generated_movie':generated_movie
        }
        
        return output
        