import curses

# game board initially filled with zeros
board = [[0 for _ in range(7)] for _ in range(6)]
player = 1

# takes window, board, and message to show at the top
def show_board(win, board, info):
    win.clear()
    h, w = win.getmaxyx()

    win.addstr(1, w//2 - len(info)//2, info)

    for i in range(6):
        for j in range(7):
            if board[i][j] != 0:
                win.attron(curses.color_pair(board[i][j]))
                win.addch(h//2 + i - 3, w//2 + j - 3, curses.ACS_BLOCK)
                win.attroff(curses.color_pair(board[i][j]))
            else:
                win.addch(h//2 + i - 3, w//2 + j - 3, curses.ACS_BLOCK)

    win.refresh()


def reset_game(win):
    board = [[0 for _ in range(7)] for _ in range(6)]

    show_board(win, board, 'Player 1 to play')


def game_over(board, player):
    # Horizontal check
    for i in range(4):
        for j in range(6):
            if (
                board[j][i] == player
                and board[j][i + 1] == player
                and board[j][i + 2] == player
                and board[j][i + 3] == player
            ):
                return True

    # Vertical check
    for i in range(7):
        for j in range(3):
            if (
                board[j][i] == player
                and board[j + 1][i] == player
                and board[j + 2][i] == player
                and board[j + 3][i] == player
            ):
                return True

    # Positive diagonal check
    for i in range(4):
        for j in range(3):
            if (
                board[j][i] == player
                and board[j + 1][i + 1] == player
                and board[j + 2][i + 2] == player
                and board[j + 3][i + 3] == player
            ):
                return True

    # Negative diagonal check
    for i in range(4):
        for j in range(3, 6):
            if (
                board[j][i] == player
                and board[j - 1][i + 1] == player
                and board[j - 2][i + 2] == player
                and board[j - 3][i + 3] == player
            ):
                return True

    return False


def get_legal_actions(board):
    legal = []
    for col in range(7):
        if board[0][col] == 0:
            legal.append(col + 1)
    return legal


def make_move(board, column, player):
    column_values = [board[row][column] for row in range(6)]
    
    for row in range(5, -1, -1):
        if column_values[row] == 0:
            board[row][column] = player
            break


def main(win):
    global player, board

    win.clear()
    curses.curs_set(0)
    h, w = win.getmaxyx()

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    reset_game(win)

    legal_moves = get_legal_actions(board)

    while True:
        column = int(win.getkey())

        if column in legal_moves:
            make_move(board, column-1, player)
            legal_moves = get_legal_actions(board)

            if game_over(board, player):
                show_board(win, board, f'Player {str(player)} has won!!')
                win.getkey()
                break

            elif len(legal_moves) == 0:
                show_board(win, board, 'Game Drawn....')
                win.getkey()
                break

            else:
                player ^= 3
                show_board(win, board, f'Player {str(player)} to play')

        else:
            show_board(win, board, f'Player {player}, please make a valid move..')


curses.wrapper(main)
