<<<<<<< HEAD
import market_data

=======
import accounts
import alpaca_trade_api as tradeapi
import re
>>>>>>> df54e50f291b9c2936163a9984f78802f47d6051
class stock:
    from accounts import access_db
    def __init__(self, ticker):
        database = accounts.access_db()
        stock_db = database.worksheet('Stocks')
        for stock_in_db in stock_db.get_all_records():
            if stock_in_db['Ticker'] == ticker:
                stock_dict = stock_in_db
                break
        self.ticker = ticker
        self.curr_price = stock_dict['Current Price']
        self.position = stock_dict['Position']
        self.dict = stock_dict
class user:
    from accounts import access_db
    def __init__(self, username):
        database = accounts.access_db()
        user_db = database.worksheet('Users')
        for user_in_db in user_db.get_all_records():
            if user_in_db['Username'] == username:
                user_dict = user_in_db
                break
        self.username = username
        self.accuracy = user_dict['Accuracy']
<<<<<<< HEAD

def update_stock(date, num_bars): #date in ISO format
    from accounts import access_db

    database = access_db()
    stock_db = database.sheet1

    for r in range(2, stock_db.row_count -990):
        row = stock_db.row_values(r)
        ticker = row[0]
        print(ticker) 
        stock_bars = market_data.get_barsets(ticker, date, num_bars)
        for i in range(0, num_bars):
            stock_db.update_cell(r, 5 + i, stock_bars[i].c)

def update_users(date):
    import public_data 

    database = accounts.access_db()
    users_db = database.sheet2

    for users in users_db.get_all_records():
        username = users['Username']
    return
=======
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
>>>>>>> df54e50f291b9c2936163a9984f78802f47d6051
