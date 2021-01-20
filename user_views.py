# I think it would be cool to have a GUI in the terminal. 
import curses
import accounts

from google.cloud import language

def language_analysis(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text,type_=language.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document':document}).document_sentiment

    return sentiment.score

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
    columns = 5
    stdscr.addstr(0,0,'Ticker')
    stdscr.addstr(0, w//columns,'Avg. Sent.')
    stdscr.addstr(0, 2*w//columns,'Sent. Std. Dev.')
    stdscr.addstr(0,3*w//columns,'Position')
    stdscr.addstr(0,4*w//columns,'Current Price')
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
        str(stock['Avg. Sent.'])
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_sentiments):
        if idx < h-1:
            x = w//columns
            y = 1 + idx
            stdscr.addstr(y,x,row)
    stocks_sentiment_stddev = [
        stock['Sent. Std. Dev.']
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_sentiment_stddev):
        if idx < h-1:
            x = 2*w//columns
            y = 1 + idx
            stdscr.addstr(y,x,row)
    stocks_positions = [
        str(stock['Position'])
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_positions):
        if idx < h-1:
            x = 3*w//columns
            y = 1 + idx
            stdscr.addstr(y,x,row)
    stocks_prices = [
        str(stock['Current Price'])
        for stock in stocks_list
        ]
    for idx, row in enumerate(stocks_prices):
        if idx < h-1:
            x = 4*w//columns
            y = 1 + idx
            stdscr.addstr(y,x,row)
    key = stdscr.getch()
    while key not in [curses.KEY_BACKSPACE]:
        key = stdscr.getch()

def portfolio_views(stdscr):
    stdscr.clear()
    alpaca = accounts.access_alpaca()
    stdscr.addstr(0,0,'Buying Power: ')
    stdscr.addstr(1,0,'Cash: ')
    stdscr.addstr(2,0,'Portfolio Value: ')
    stdscr.refresh()
    stdscr.addstr(0, 14,alpaca.get_account().buying_power)
    stdscr.addstr(1,6, alpaca.get_account().cash)
    stdscr.addstr(2, 17, alpaca.get_account().portfolio_value)
    key = stdscr.getch()
    while key not in [curses.KEY_BACKSPACE]:
        key = stdscr.getch()
def posts_views(stdscr):
    stdscr.clear()
    related_tickers = ['PLTR, GME', 'AMZN, TSLA','BA', 'BABA']
    h, w = stdscr.getmaxyx()
    columns = 3
    rows = 10
    stdscr.addstr(0,0,'Post')
    stdscr.addstr(0, w//columns,'Related Tickers')
    stdscr.addstr(0,2*w//columns,'Sentiment')
    stdscr.refresh()

    reddit = accounts.access_reddit()
    posts_titles_text = []

    for submission in reddit.subreddit('wallstreetbets').hot(limit=rows):
        posts_titles_text.append([submission.title, submission.selftext])

    current_row_idx = 0
    sentiment_values = []
    while 1: 
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        columns = 3
        stdscr.addstr(0,0,'Post')
        stdscr.addstr(0, w//columns,'Related Tickers')
        stdscr.addstr(0,2*w//columns,'Sentiment')
        stdscr.refresh()
        for idx, row in enumerate(posts_titles_text):

            if idx < h-1:
                x = 0
                y = 1 + idx
                if idx == current_row_idx:
                    stdscr.attron(curses.color_pair(1))
                    if len(row[0]) >= 20:
                        stdscr.addstr(y,x,row[0][0:17]+'...')
                    else:
                        stdscr.addstr(y,x,row[0])
                    stdscr.attroff(curses.color_pair(1))
                else: 
                    if len(row[0]) >= 20:
                        stdscr.addstr(y,x,row[0][0:17]+'...')
                    else:
                        stdscr.addstr(y,x,row[0])

        for idx, row in enumerate(related_tickers):
            if idx < h-1:
                x = w//columns
                y = 1 + idx
                stdscr.addstr(y,x,row)
        stdscr.refresh()
        if not sentiment_values:
            sentiment_values = calculate_render_sentiment(stdscr, posts_titles_text, h, w, columns)
        else:
            for idx, row in enumerate(sentiment_values):
                x = 2*w//columns
                y = 1 + idx
                stdscr.addstr(y,x,sentiment_values[idx])
                stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row_idx >= 1:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < h-2 and current_row_idx < rows-1:
            current_row_idx += 1
        elif key == curses.KEY_BACKSPACE:
            break
        elif key in [curses.KEY_ENTER, 10, 13]:
            single_post_view(stdscr, posts_titles_text[current_row_idx], h, w)
def calculate_render_sentiment(stdscr,posts_titles_text, height, width, columns):
    sentiment = []
    for idx, row in enumerate(posts_titles_text):
        sentiment.append(str(language_analysis(row[1])))
        if idx < height-1:
            x = 2*width//columns
            y = 1 + idx
            stdscr.addstr(y,x,sentiment[idx])
            stdscr.refresh()
        else:
            break
    return sentiment
def single_post_view(stdscr,posts_titles_text, height, width):
    stdscr.clear()
    stdscr.addstr(0,0, posts_titles_text[0])
    stdscr.addstr(5,0, posts_titles_text[1][0:width*(height-5)]) #This is sometimes too long
    key = stdscr.getch()
    stdscr.refresh()
    while key not in [curses.KEY_BACKSPACE]:
        key = stdscr.getch()

def main(stdscr):
    menu = ['Stocks','Portfolio', 'Posts']
    curses.curs_set(0)

    current_row_idx = 0
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    print_menu(stdscr, menu, current_row_idx)

    
    while 1:

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row_idx >= 1:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_BACKSPACE:
            break
        elif key in [curses.KEY_ENTER, 10, 13]:
            if menu[current_row_idx] == 'Stocks':
                stocks_views(stdscr)
            elif menu[current_row_idx] == 'Portfolio':
                portfolio_views(stdscr)
            elif menu[current_row_idx] == 'Posts':
                posts_views(stdscr)
        
        print_menu(stdscr, menu, current_row_idx)
def run():
    curses.wrapper(main)
    curses.endwin()
