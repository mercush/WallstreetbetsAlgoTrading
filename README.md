# WallstreetbetsAlgoTrading
Trades based on sentiment analysis from reddit.com/wallstreetbets

## An Update
1. `vim ~/.bashrc`
2. Go to the very bottom and you'll see something like "alias wsb-utils ..."
3. Replace `bash ${DIR}/bash-utils` with `source ${DIR}/bash-utils`
## Getting Started: 
1. Make sure you have virtualenv and gpg installed. It's probably `pip3 install virtualenv`
2. `bash ./bash-utils.sh s`

## Sentiment analysis:
Here is a good resource for [Sentiment Analysis](https://realpython.com/sentiment-analysis-python/). I think it's better if we use the Google Cloud Natural Language Processing API since it's probably been trained more and sentiment analysis is mostly available out of the box. 

## Documentation for stuff:
- Reddit API: [PRAW](https://praw.readthedocs.io/en/latest/)
    - Here is another good resource for [scraping Reddit](https://www.storybench.org/how-to-scrape-reddit-with-python/).
- Amazon AWS API: [BOTO3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - This is so we can run the script all day when we're at that stage. Google cloud API would probably be better since it's free
- ALPACA Trading API: [ALPACA](https://alpaca.markets/docs/api-documentation/)
     - We can use another API in the future like Webull or etrade. I think this is a good place to start though
- Google Sheets Databased: [Google Sheets](https://gspread.readthedocs.io/en/latest/)
     - This is where we store data on a remote server