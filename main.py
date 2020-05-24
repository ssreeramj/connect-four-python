import curses

menu = ['Home', 'Play', 'Scorecard', 'Exit']

def show_menu(stdscr, current_index):
    h, w = stdscr.getmaxyx()

    for ind, item in enumerate(menu):
        height = h//2 - len(menu)//2 + ind
        width = w//2 - len(item)//2
        
        if ind == current_index:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(height, width, item)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(height, width, item)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    h, w = stdscr.getmaxyx()
    
    current_index = 0
    show_menu(stdscr, current_index)
    
    while True:        
        key = stdscr.getch()    

        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1

        elif key == curses.KEY_DOWN and current_index < len(menu) - 1:
            current_index += 1

        elif key == 10:
            if current_index == len(menu) - 1:
                break
            stdscr.clear()
            message = f'You clicked on {menu[current_index]}'
            stdscr.addstr(h//2, w//2 - len(message)//2, message )
            stdscr.refresh()
            stdscr.getkey()

        stdscr.clear()
        show_menu(stdscr, current_index)

curses.wrapper(main)