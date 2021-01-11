import praw
import alpaca_trade_api as tradeapi
import re
from google.cloud import language

import accounts
import db_man
import user_views

def language_analysis(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text,type_=language.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document':document}).document_sentiment

    print("Test: {}".format(text))
    print('Sentiment: {}, {}'.format(sentiment.score,sentiment.magnitude))
    return 0
if __name__ == '__main__':
    language_analysis(
        'PLTR sucks'
    )
    user_views.run()
