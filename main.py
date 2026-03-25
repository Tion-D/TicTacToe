import os
from datetime import date

EMPTY = "_"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def step_to_idx(step):
    step -= 1
    return step // 3, step % 3


def idx_to_step(row, col):
    return row * 3 + col + 1


def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def print_board(board):
    clear_screen()
    print("Tic-Tac-Toe")
    print("Positions:")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|")
    print("\nBoard:")
    for row in board:
        print("|" + "|".join(row) + "|")


def is_empty(board, step):
    if not 1 <= step <= 9:
        return False
    row, col = step_to_idx(step)
    return board[row][col] == EMPTY


def place(board, step, mark):
    row, col = step_to_idx(step)
    board[row][col] = mark


def get_empty_steps(board):
    steps = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                steps.append(idx_to_step(row, col))
    return steps


def check_win(board, mark):
    lines = []

    lines.extend(board)

    for col in range(3):
        lines.append([board[row][col] for row in range(3)])

    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    return any(all(cell == mark for cell in line) for line in lines)


def is_tie(board):
    return not get_empty_steps(board)


def get_player_mark():
    while True:
        choice = input("Choose X or O: ").strip().lower()
        if choice in ("x", "o"):
            return choice
        print("Please enter only X or O.")


def get_player_move(board):
    while True:
        try:
            step = int(input("Choose a number between 1 and 9: "))
        except ValueError:
            print("Not a number.")
            continue

        if not 1 <= step <= 9:
            print("Pick 1-9.")
            continue
        if not is_empty(board, step):
            print("That spot is taken.")
            continue
        return step


def computer_move(board, computer_mark, player_mark):
    for step in get_empty_steps(board):
        place(board, step, computer_mark)
        if check_win(board, computer_mark):
            return
        place(board, step, EMPTY)

    for step in get_empty_steps(board):
        place(board, step, player_mark)
        if check_win(board, player_mark):
            place(board, step, computer_mark)
            return
        place(board, step, EMPTY)

    priority = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    for step in priority:
        if is_empty(board, step):
            place(board, step, computer_mark)
            return


def main():
    player_mark = get_player_mark()
    computer_mark = "o" if player_mark == "x" else "x"
    board = create_board()

    print(f"\nYou chose {player_mark.upper()}")

    turn = "x"

    while True:
        print_board(board)

        if turn == player_mark:
            step = get_player_move(board)
            place(board, step, player_mark)

            if check_win(board, player_mark):
                print_board(board)
                print("You won!")
                break
        else:
            computer_move(board, computer_mark, player_mark)

            if check_win(board, computer_mark):
                print_board(board)
                print("The computer won!")
                break

        if is_tie(board):
            print_board(board)
            print("Tie game!")
            break

        turn = "o" if turn == "x" else "x"


if __name__ == "__main__":
    main()
