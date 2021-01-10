import accounts
import alpaca_trade_api as tradeapi
import re
class stock:
    def __init__(self, ticker):
        database = accounts.access_db()
        stock_db = database.worksheet('Stocks')
        for stock_in_db in stock_db.get_all_records():
            if stock_in_db['Ticker'] == ticker:
                stock_dict = stock_in_db
                break
        self.ticker = ticker
        self.price = stock_dict['Price']
        self.position = stock_dict['Position']
        self.dict = stock_dict
class user:
    def __init__(self, username):
        database = accounts.access_db()
        user_db = database.worksheet('Users')
        for user_in_db in user_db.get_all_records():
            if user_in_db['Username'] == username:
                user_dict = user_in_db
                break
        self.username = username
        self.accuracy = user_dict['Accuracy']
        self.dict = user_dict
def convert_list_to_string(list_input):
    return str(list_input)
def convert_string_to_list(string_input):
    return re.split(r'["\'], ["\']',string_input.strip('[\'" ]'))
def update_db():
    database = accounts.access_db()
    stock_db = database.worksheet('Stocks')
    alp = accounts.access_alpaca()

    for stock_in_db in stock_db.get_all_records():
        ticker = stock_in_db['Ticker'] 
        barset = alp.get_barset(ticker, ' day', limit=1)
        stock_bar = barset[ticker]
        print(stock_bar)
        stock_db.update_cell(ticker.row, ticker.col + 2, stock_bar.c)
