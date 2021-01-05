# I think it would be cool to have a GUI in the terminal. 
import curses

menu = ['Stocks','Portfolio']
def print_menu(stdscr, selected_row_idx):
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
    stdscr.addstr(0,0, "This is the stocks view")
def portfolio_views(stdscr):
    stdscr.addstr(0,0, "This is the portfolio view")
def main(stdscr):
    curses.curs_set(0)

    current_row_idx = 0
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    print_menu(stdscr, current_row_idx)

    
    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx >= 1:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if menu[current_row_idx] == 'Stocks':
                stocks_views(stdscr)
            elif menu[current_row_idx] == 'Portfolio':
                portfolio_views(stdscr)
            stdscr.refresh()
            stdscr.getch()

        print_menu(stdscr, current_row_idx)

curses.wrapper(main)
curses.endwin()