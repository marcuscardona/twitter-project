class stringUtils():
    def remove_first_non_alphabetic_chars(self, text):
        """
        Definition: removes in-place first non alphabetic characters from string `text`
        Inputs:
            `text`, string
        Outputs:
            `text`, string without first non alphabetic characters
        Author:
            @joaoreboucas1
        Since:
            03-2023
        """
        while True:
            if not text[0].isalpha():
                text = text[1:]
            else:
                return text
    
    def turn_long_text_into_subtexts(self, long_text, subtext_length):
        """
        Separates a long string into a list of strings whose length is less than `subtext_length`.

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
            if length < subtext_length-len(word):
                tweets[number_of_tweets-1] += word+' '
            else:
                tweets.append('')
                number_of_tweets += 1
                tweets[number_of_tweets-1] += word+' '
        return tweets