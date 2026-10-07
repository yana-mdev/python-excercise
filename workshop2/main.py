class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix_):
    for row in matrix_:
        print(row)


def validate_column_choice(col_, max_index):
    if not (0 <= col_ < max_index):
        raise InvalidColumnError


def place_player_choice(matrix_, c ,player_num):
    for r in range(len(matrix_) - 1, -1 ,-1):
        if matrix_[r][c] == 0:
            matrix_[r][c] = player_num
            return r, c
    raise FullColumnError()


def is_player_num(matrix_, r, c, player_num):
    if r < 0 or c < 0 or r >= len(matrix_) or c >= len(matrix_[0]):
        return False
    return matrix_[r][c] == player_num


def check_row_winner(matrix_, r, c, player_num, slots):
    filled = 1

    for index in range(1, slots):
        if is_player_num(matrix_, r, c + index, player_num):
            filled += 1
        else:
            break

    for index in range(1, slots):
        if is_player_num(matrix_, r, c - index, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def check_col_winner(matrix_, r, c, player_num, slots):
    return all(is_player_num(matrix_, r + index, c, player_num) for index in range(slots))


def check_left_diagonal_winner(matrix_, r, c, player_num, slots):
    filled = 1

    for index in range(1, slots):
        if is_player_num(matrix_, r - index, c - index, player_num):
            filled += 1
        else:
            break

    for index in range(1, slots):
        if is_player_num(matrix_, r + index, c + index, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def check_right_diagonal_winner(matrix_, r, c, player_num, slots):
    filled = 1

    for index in range(1, slots):
        if is_player_num(matrix_, r - index, c + index, player_num):
            filled += 1
        else:
            break

    for index in range(1, slots):
        if is_player_num(matrix_, r + index, c - index, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def check_for_winner(matrix_, r, c, player_num, slots):
    return (check_row_winner(matrix_, r, c, player_num, slots)
        or check_col_winner(matrix_, r, c, player_num, slots)
        or check_right_diagonal_winner(matrix_, r, c, player_num, slots)
        or check_left_diagonal_winner(matrix_, r, c, player_num, slots))


ROWS = 6
COLS = 7
SLOTS = 4

matrix = create_matrix(ROWS, COLS)

print_matrix(matrix)

player_number = 1
counter = 0

while True:
    try:
        column_num = int(input(f"Player {player_number}, please choose a column:\n")) - 1
        validate_column_choice(column_num, COLS)
        row, col = place_player_choice(matrix, column_num, player_number)
        print_matrix(matrix)

        if check_for_winner(matrix, row, col, player_number, SLOTS):
            print(f"Player {player_number} wins!")
            break

        counter += 1
        if ROWS * COLS == counter:
            print(f"Draw!")
            break

        player_number = 2 if player_number == 1 else 1
    except ValueError:
        print("Please enter a valid number!")
    except InvalidColumnError:
        print(f"Please select a column between 1 and {COLS}")
    except FullColumnError:
        print(f"Position is already occupied! Please choose another!")