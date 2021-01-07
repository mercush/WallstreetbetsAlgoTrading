import accounts
import alpaca_trade_api as tradeapi
class stock:
    def __init__(self, ticker):
        database = accounts.access_db()
        stock_db = database.sheet1
        for stock_in_db in stock_db.get_all_records():
            if stock_in_db['Ticker'] == ticker:
                stock_dict = stock_in_db
                break
        self.ticker = ticker
        self.price = stock_dict['Price']
        self.position = stock_dict['Position']

class user:
    def __init__(self, username):
        database = accounts.access_db()
        user_db = database.sheet2
        for user_in_db in user_db.get_all_records():
            if user_in_db['Username'] == username:
                userf_dict = user_in_db
                break
        self.username = username
        self.accuracy = user_dict['Accuracy']

def update_db():
    database = accounts.access_db()
    stock_db = database.sheet1
    alp = tradeapi.REST()

    for stock_in_db in stock_db.get_all_records():
        ticker = stock_in_db['Ticker'] 
        barset = alp.get_barset(ticker.value, ' day', limit=1)
        stock_bar = barset[ticker]
        database.update_cell(ticker.row, ticker.col + 2, stock_bar.c)