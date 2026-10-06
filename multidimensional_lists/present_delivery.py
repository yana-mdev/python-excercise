presents = int(input())
n = int(input())

matrix = []
santa_r, santa_c = 0, 0
nice_kids = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa_r, santa_c = row, col
        elif matrix[row][col] == "V":
            nice_kids += 1


DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

nice_kids_with_present = 0

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    dr, dc = DIRECTIONS[command]
    row, col = santa_r + dr, santa_c + dc
    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "V":
            presents -= 1
            nice_kids_with_present += 1
        elif matrix[row][col] == "C":
            for direction_row, direction_col in DIRECTIONS.values():
                new_row = row + direction_row
                new_col = col + direction_col
                if presents == 0:
                    break
                if 0 <= new_row < n and 0 <= new_col < n:
                    if matrix[new_row][new_col] == "V":
                        presents -= 1
                        nice_kids_with_present += 1
                    elif matrix[new_row][new_col] == "X":
                        presents -= 1
                    matrix[new_row][new_col] = "-"
        matrix[santa_r][santa_c] = "-"
        santa_r, santa_c = row, col
        matrix[santa_r][santa_c] = "S"

remaining_kids = nice_kids - nice_kids_with_present
if presents == 0 and remaining_kids > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if remaining_kids > 0:
    print(f"No presents for {remaining_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_with_present} happy nice kid/s.")




