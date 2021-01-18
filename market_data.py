
def time_to_market_close():
    from accounts import access_alpaca
    clock = access_alpaca.get_clock()
    return (clock.next_close - clock.timestamp).total_seconds()

def past_market_timeframe(date): # date in format year-month-day
    from accounts import access_alpaca
    calendar = access_alpaca.get_calendar(start=date, end=date)[0]
    return (calendar.open, calendar.close)

def get_barsets(ticker, time_start, limit):
    from accounts import access_alpaca
    api = access_alpaca()
    fts = time_start
    lim = limit
    barset = api.get_barset(ticker, 'day', limit= lim, start=fts, end=None, after=None, until=None)
    #barset = api.get_barset(ticker, 'day', limit = lim)
    bars = barset[ticker]
    print(bars[0].o)
    return barset[ticker]