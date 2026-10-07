import tkinter as tk
from tkinter import messagebox


ROWS = 6
COLS = 7
SLOTS = 4

class FullColumnError(Exception):
    pass


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def place_player_choice(matrix_, c ,player_num):
    for r in range(len(matrix_) - 1, -1 ,-1):
        if matrix_[r][c] == 0:
            matrix_[r][c] = player_num
            return r, c
    raise FullColumnError()


def is_player_num(matrix_, r, c, player_n):
    if r < 0 or c < 0 or r >= len(matrix_) or c >= len(matrix_[0]):
        return False
    return matrix_[r][c] == player_n


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


def update_ui(labels_, row_, col_, player_num):
    color = "red" if player_num == 1 else "blue"
    labels_[row_][col_].config(bg=color)


def reset_game(matrix_, labels_):
    for r in range(len(matrix_)):
        for c in range(len(matrix_[0])):
            matrix_[r][c] = 0
            labels_[r][c].config(bg="white")


def handle_column_click(matrix_, labels_, column_, player_n, slots_, counter_):
    try:
        row, column_num = place_player_choice(matrix_, column_, player_n)
        update_ui(labels_, row, column_num, player_n)

        if check_for_winner(matrix_, row, column_num, player_n, slots_):
            messagebox.showinfo("Game over!", f"Player {player_n} wins!")
            reset_game(matrix_, labels_)
            return 1, 0

        counter_ += 1

        if ROWS * COLS == counter_:
            messagebox.showinfo("Game over!", f"The game is draw!")
            reset_game(matrix_, labels_)
            return 1, 0

    except FullColumnError:
        messagebox.showerror("Full Column Error", "Position is already occupied! Please select another column.")

    return 2 if player_n == 1 else 1, counter_


def create_ui(root, rows, cols, slots):
    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text=" ", relief="solid", width=16, height=6) for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row=r+1, column=c)

    player_state = {"player_num": 1, "counter": 0}

    def on_click(column_num, p_state):
        p_state["player_num"], p_state["counter"] = handle_column_click(matrix, labels, column_num, player_state["player_num"], rows, cols, slots, player_state["counter"])


    buttons = [tk.Button(root, text="⬇", width=16, height=6, bg="yellow", command=lambda c_idx=col: on_click(c_idx, player_state)) for col in range(cols)]
    for col, button in enumerate(buttons):
        button.grid(row=0, column=col)


def start_game():
    root = tk.Tk()
    root.title("Connect Four")

    create_ui(root, ROWS, COLS, SLOTS)

    root.mainloop()



if __name__ == '__main__':
    start_game()