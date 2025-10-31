import social_tests as test

### PHASE 1 ###

import pandas as pd
import nltk
nltk.download('vader_lexicon', quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def parse_label(label):
    return 

def get_region_from_state(state_df, state):
    return 

end_chars = [ " ", "\n", "#", ".", ",", "?", "!", ":", ";", ")" ]
def find_hashtags(message):
    return 

def find_sentiment(classifier, message):
    return 

def add_columns(data, state_df):
    return

### PHASE 2 ###

def get_sentiment_quantiles(data, col_name, col_value):
    return 

def get_hashtag_subset(data, col_name, col_value):
    return 

def get_hashtag_rates(data):
    return 

def most_common_hashtags(hashtags, count):
    return 

def get_hashtag_sentiment(data, hashtag):
    return 

### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.test_all()
    test.run()