import sys,os
import curses

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.refresh()

    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)

    host = "Hostname: localhost"
    port = "Port: 3306"
    user = "Username: archa"
    pwd = "Password: Archa123"

    menu = [host, port, user, pwd, 'Exit']

    current_row = 0

    # title
    title = "Insert data model database parameter"
    start_x_title = int((w // 2) - (len(title) // 2) - len(title) % 2)
    start_y = int((h // 2) - 4)
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(start_y, start_x_title, title)
    stdscr.attroff(curses.A_BOLD)
    stdscr.refresh()

    topnote = "New Archiving Distributed InfrastructuRe"
    stdscr.addstr(0, 0, topnote, curses.color_pair(1))

    footnote = "Tab/Alt-Tab"

    # Render status bar
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(h-1, 0, footnote)
    stdscr.addstr(h-1, len(footnote), " " * (w - len(footnote) - 1))
    stdscr.attroff(curses.color_pair(3))


    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
        stdscr.refresh()

    while (k != ord('q')):
        k = stdscr.getch() 

        if k == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP and current_row > 0:
            current_row -= 1
            cursor_y = cursor_y - 1
        elif k == curses.KEY_ENTER or k in [10, 13]:
            break

        for idx, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = h//2 - len(menu)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
