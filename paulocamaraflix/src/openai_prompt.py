from dotenv import load_dotenv
import os
from pathlib import Path
import random
import openai

class openaiPrompt():

    def __init__(self):
        load_dotenv()
        self._api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self._api_key

    def read_prompt(self, filename):
        """
        Looks in prompts/ directory for a text file. Pass in file name only, not extension.
        Example: prompts/hello-world.txt -> read_prompt('hello-world')

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
        query = movie_prompt.format(
            random.choice(self.read_prompt('genres').split('\n'))
          , random.choice(self.read_prompt('directors').split('\n'))
          , random.choice(self.read_prompt('protagonist_name').split('\n'))
          , random.choice(self.read_prompt('protagonist_surname').split('\n'))
          , random.choice(self.read_prompt('occupations').split('\n'))
          , random.choice(self.read_prompt('occupation_complements').split('\n'))          
          , random.choice(self.read_prompt('adjectives').split('\n'))
          , random.choice(self.read_prompt('roles').split('\n'))
          , random.choice(self.read_prompt('famous_people').split('\n'))
          
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
        
        return generated_movie