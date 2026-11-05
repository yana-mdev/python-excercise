n = int(input())

matrix = []

bee_row, bee_col = 0, 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "B":
            bee_row, bee_col = row, col
            matrix[row][col] = "-"


MAPPER = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

initial_energy = 15
nectar = 0
reached_hive = False
restored = False

while initial_energy > 0:
    command = input()
    dr, dc = MAPPER[command]

    bee_row = (bee_row + dr) % n
    bee_col = (bee_col + dc) % n

    initial_energy -= 1

    current_cell = matrix[bee_row][bee_col]

    if current_cell.isdigit():
        nectar += int(current_cell)
        matrix[bee_row][bee_col] = "-"
    elif current_cell == "H":
        reached_hive = True
        break

    if initial_energy == 0:
        if nectar >= 30 and not restored:
            initial_energy += nectar - 30
            nectar = 30
            restored = True
        if initial_energy == 0:
            break


if reached_hive:
    if nectar >= 30:
        print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
    else:
        print("Beesy did not manage to collect enough nectar.")
else:
    print("This is the end! Beesy ran out of energy.")


matrix[bee_row][bee_col] = "B"
for row in matrix:
    print("".join(row))




