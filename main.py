<<<<<<< HEAD
import praw
import alpaca_trade_api as tradeapi
import re
from google.cloud import language

import accounts
from db_man import *
=======
>>>>>>> df54e50f291b9c2936163a9984f78802f47d6051
import user_views

if __name__ == '__main__':
<<<<<<< HEAD
    # reddit = accounts.access_reddit()
    # alpaca = accounts.access_alpaca()
    # reddit_submissions_data(reddit)
    # language_analysis(
    #     'this is text test'
    # )
    update_stock('2019-04-15T09:30:00-4:00', 10)
    user_views.run()  
=======
    user_views.run()
>>>>>>> df54e50f291b9c2936163a9984f78802f47d6051
