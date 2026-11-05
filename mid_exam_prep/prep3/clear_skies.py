n = int(input())

matrix = []
jet_row, jet_col = 0, 0
enemy_count = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "J":
            jet_row, jet_col = row, col
            matrix[row][col] = "-"
        elif matrix[row][col] == "E":
            enemy_count += 1


MAPPER = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

initial_armor = 300

while initial_armor > 0:
    command = input()
    dr, dc = MAPPER[command]

    new_row, new_col = jet_row + dr, jet_col + dc

    if matrix[new_row][new_col] == "E":
        matrix[new_row][new_col] = "-"
        enemy_count -= 1
        if enemy_count == 0:
            jet_row, jet_col = new_row, new_col
            print(f"Mission accomplished, you neutralized the aerial threat!")
            break
        initial_armor -= 100

    elif matrix[new_row][new_col] == "R":
        initial_armor = 300
        matrix[new_row][new_col] = "-"

    jet_row, jet_col = new_row, new_col

    if initial_armor <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
        break


matrix[jet_row][jet_col] = "J"
for row in matrix:
    print(*row, sep="")