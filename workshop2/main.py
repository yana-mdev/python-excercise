class InvalidColumnError(Exception):
    pass


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix_):
    for row in matrix_:
        print(row)


def validate_column_choice(col_, max_index):
    if not (0 <= col_ < max_index):
        raise InvalidColumnError


ROWS = 6
COLS = 7

matrix = create_matrix(ROWS, COLS)

print_matrix(matrix)


while True:
    player_number = 1
    try:
        column_num = int(input(f"Player {player_number}, please choose a column:\n")) - 1
        validate_column_choice(column_num, COLS)

        player_number = 2 if player_number == 1 else 1
    except ValueError:
        print("Please enter a valid number!")
    except InvalidColumnError:
        print(f"Please select a column between 1 and {COLS}")