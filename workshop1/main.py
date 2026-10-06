player_one_name = input("Player one name: ")
player_two_name = input("Player two name: ")
player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

while player_one_sign not in ["X", "O"]:
    print("Please enter either 'X' or 'O'.")
    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

player_two_sign = 'O' if player_one_sign == 'X' else 'X'

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"{player_one_name} starts first!")


def check_row_winner(board_, current_sign_):
    for row_ in board_:
        if row_.count(current_sign_) == 3:
            return True
    return False


def check_col_winner(board_, current_sign_):
    for col_index in range(3):
        count = 0
        for row_index in range(3):
            if board_[row_index][col_index] == current_sign_:
                count += 1
        if count == 3:
            return True
    return False


def check_diagonal_winner(board_, current_sign_):
    count_primary = 0
    count_secondary = 0
    for index in range(3):
        if board[index][index] == current_sign_:
            count_primary += 1
        if board[index][3 - index - 1] == current_sign_:
            count_secondary += 1
    if count_primary == 3 or count_secondary == 3:
        return True
    return False


def check_for_winner(board_, current_sign_):
    if check_row_winner(board_, current_sign_) or check_col_winner(board_, current_sign_) or check_diagonal_winner(board_, current_sign_):
        return True
    return False


def print_board(board_):
    for row_ in board_:
        print(f"| {' | '.join(row_)} |")


turn = 1
board = [[" ", " ", " "] for _ in range(3)]
MAPPER = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

while turn < 10:
    current_player = player_one_name if turn % 2 != 0 else player_two_name
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    try:
        position = int(input(f"{current_player} please choose a free position [1-9]: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if not (1 <= position <= 9):
        print("Please enter a valid number between 1 and 9!")
        continue

    row, col = MAPPER[position]
    if board[row][col] != " ":
        print("This position is already occupied!")
        continue

    board[row][col] = current_sign
    print_board(board)

    if turn >= 5 and check_for_winner(board, current_sign):
        print(f"Congrats! {current_player} is a winner!")
        break

    turn += 1
else:
    print("Thanks for playing, no winner today!")