n = int(input())

matrix = []
pacman_row, pacman_col = 0, 0
remaining_stars = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "P":
            pacman_row, pacman_col = row, col
            matrix[row][col] = "-"
        elif matrix[row][col] == "*":
            remaining_stars += 1


MAPPER = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

initial_health = 100
has_immunity = False


while True:
    command = input()
    if command == "end":
        break

    dr, dc = MAPPER[command]
    new_row = (pacman_row + dr) % n
    new_col = (pacman_col + dc) % n

    if matrix[new_row][new_col] == "*":
        matrix[new_row][new_col] = "-"
        remaining_stars -= 1
    elif matrix[new_row][new_col] == "G":
        matrix[new_row][new_col] = "-"
        if has_immunity:
            has_immunity = False
        else:
            initial_health -= 50
        if initial_health <= 0:
            pacman_row, pacman_col = new_row, new_col
            print(f"Game over! Pacman last coordinates [{new_row},{new_col}]")
            break
    elif matrix[new_row][new_col] == "F":
        matrix[new_row][new_col] = "-"
        has_immunity = True

    pacman_row, pacman_col = new_row, new_col

    if remaining_stars == 0:
        print(f"Pacman wins! All the stars are collected.")
        break


if initial_health > 0 and remaining_stars > 0:
    print("Pacman failed to collect all the stars.")


print(f"Health: {initial_health}")
if remaining_stars > 0:
    print(f"Uncollected stars: {remaining_stars}")

matrix[pacman_row][pacman_col] = "P"
for row in matrix:
    print(*row, sep="")