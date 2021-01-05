import praw
import alpaca_trade_api as tradeapi
import re
from google.cloud import language

import accounts
import db_man
import user_views

def reddit_submissions_data(reddit):
    for submission in reddit.subreddit("wallstreetbets").hot(limit=10):
        print('TITLE: {}'.format(submission.title))
        print('BODY: {}'.format(submission.selftext))
    if re.findall('GME|PLTR',submission.title):
        print('\t {} was found in {}'.format(re.findall('GME|PLTR',
            submission.title), submission.title))
    elif  re.findall('GME|PLTR',submission.selftext):
        print('\t {} was found in {}'.format(re.findall('GME|PLTR',
            submission.title), submission.title))
def analyze_from_reddit(reddit):
    for submission in reddit.subreddit('wallstreetbets').hot(limit=10):
        language_analysis(submission.selftext)
def language_analysis(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text,type_=language.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document':document}).document_sentiment

    print("Test: {}".format(text))
    print('Sentiment: {}, {}'.format(sentiment.score,sentiment.magnitude))
    return 0
if __name__ == '__main__':
    # reddit = accounts.access_reddit()
    # alpaca = accounts.access_alpaca()
    # reddit_submissions_data(reddit)
    # language_analysis(
    #     'this is text test'
    # )
    user_views.run()