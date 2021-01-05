import re

def get_credentials_file():
    f = open('Credentials/Credentials.txt','r')
    content = f.read()
    f.close()
    return content

def access_db():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/google_credentials.json',scope)
    client = gspread.authorize(creds)
    database = client.open("WSB Trading")

    return database

def access_alpaca():
    import alpaca_trade_api as tradeapi
    content = get_credentials_file()
    keyid = re.findall('Alpaca Key ID: ([^\n]+)\n', content, re.MULTILINE)[0]
    secretkey = re.findall('^Alpaca Secret Key: ([^\n]+)\n', content, re.MULTILINE)[0]
    alpaca = tradeapi.REST(keyid, secretkey,
        base_url='https://paper-api.alpaca.markets')
    return alpaca

def access_reddit():
    import praw
    content = get_credentials_file()
    clientid = re.findall('Reddit Client ID: ([^\n]+)\n', content, re.MULTILINE)[0]
    clientsecret = re.findall('Reddit Client Secret: ([^\n]+)\n', content, re.MULTILINE)[0]
    reddit = praw.Reddit(
    client_id = clientid,
    client_secret = clientsecret,
    user_agent = "Wallstreetbetsalgotrading",
    )
    return reddit
