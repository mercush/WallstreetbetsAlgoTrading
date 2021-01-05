# I think it would be cool to have a GUI in the terminal. 
import curses
import accounts

def print_menu(stdscr, menu, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def stocks_views(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    columns = 4
    stdscr.addstr(0,0,'Ticker')
    stdscr.addstr(0, w//columns,'Sentiment')
    stdscr.addstr(0,2*w//columns,'Position')
    stdscr.addstr(0,3*w//columns,'Price')
    stdscr.refresh()
    database = accounts.access_db()
    stocks_list = database.worksheet('Stocks').get_all_records()
    stocks_tickers = [
        stock['Ticker']
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_tickers):
        if idx < h-1:
            x = 0
            y = 1 + idx
            stdscr.addstr(y,x,row)
    stocks_sentiments = [
        str(stock['Sentiment'])
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_sentiments):
        if idx < h-1:
            x = w//columns
            y = 1 + idx
            stdscr.addstr(y,x,row)
    stocks_positions = [
        str(stock['Position'])
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_positions):
        if idx < h-1:
            x = 2*w//columns
            y = 1 + idx
            stdscr.addstr(y,x,row)
    stocks_prices = [
        str(stock['Price'])
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_prices):
        if idx < h-1:
            x = 3*w//columns
            y = 1 + idx
            stdscr.addstr(y,x,row)

def portfolio_views(stdscr):
    stdscr.clear()
    alpaca = accounts.access_alpaca()
    stdscr.addstr(0,0,'Buying Power: ')
    stdscr.addstr(1,0,'Cash: ')
    stdscr.addstr(2,0,'Portfolio Value: ')
    stdscr.refresh()
    stdscr.addstr(0, 14,alpaca.get_account().buying_power)
    stdscr.addstr(1,7, alpaca.get_account().cash)
    stdscr.addstr(2, 17, alpaca.get_account().portfolio_value)
    stdscr.refresh()
def posts_views(stdscr):
    return 0
def main(stdscr):
    menu = ['Stocks','Portfolio', 'Posts', 'Exit']
    curses.curs_set(0)

    current_row_idx = 0
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    print_menu(stdscr, menu, current_row_idx)

    
    while 1:

        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx >= 1:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row_idx] == 'Stocks':
                stocks_views(stdscr)
            elif menu[current_row_idx] == 'Portfolio':
                portfolio_views(stdscr)
            elif menu[current_row_idx] == 'Posts':
                posts_views(stdscr)
            elif menu[current_row_idx] == 'Exit':
                break
            stdscr.getch()

        print_menu(stdscr, menu, current_row_idx)
def run():
    curses.wrapper(main)
    curses.endwin()