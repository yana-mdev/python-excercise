
n, m = map(int, input().split(", "))

matrix = []
ct_row, ct_col = 0, 0
bomb_row, bomb_col = 0, 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "C":
            ct_row, ct_col = row, col
            matrix[row][col] = "*"
        elif matrix[row][col] == "B":
            bomb_row, bomb_col = row, col

start_row, start_col = ct_row, ct_col

MAPPER = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

time_in_secs = 16
bomb_defused = False
terrorist_killed = False
bomb_exploded = False
defuse_failed = False
needed_time = 0

while time_in_secs > 0:
    command = input()

    if command == "defuse":
        if (ct_row, ct_col) == (bomb_row, bomb_col):
            if time_in_secs >= 4:
                time_in_secs -= 4
                matrix[bomb_row][bomb_col] = "D"
                bomb_defused = True
            else:
                needed_time = 4 - time_in_secs
                matrix[bomb_row][bomb_col] = "X"
                defuse_failed = True
            break
        else:
            time_in_secs -= 2
    else:
        time_in_secs -= 1
        dr, dc = MAPPER[command]
        new_r, new_c = ct_row + dr, ct_col + dc

        if 0 <= new_r < n and 0 <= new_c < m:
            ct_row, ct_col = new_r, new_c

            if matrix[ct_row][ct_col] == "T":
                matrix[ct_row][ct_col] = "*"
                terrorist_killed = True
                break

    if time_in_secs <= 0:
        bomb_exploded = True
        break

if bomb_defused:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {time_in_secs} second/s remaining.")
elif terrorist_killed:
    print("Terrorists win!")
elif bomb_exploded or defuse_failed:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {needed_time} second/s.")

if not terrorist_killed:
    matrix[start_row][start_col] = "C"

for row in matrix:
    print("".join(row))
