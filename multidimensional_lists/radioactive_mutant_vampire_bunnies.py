def spread_bunnies(matrix, bunnies_set):
    new_bunnies_set = set()
    for b_row, b_col in bunnies_set:
        for d_row, d_col in MOVES.values():
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < n and 0 <= new_col < m:
                matrix[new_row][new_col] = "B"
                new_bunnies_set.add((new_row, new_col))
    bunnies_set.update(new_bunnies_set)


n, m = map(int, input().split())

lair = []
p_row, p_col = 0, 0
bunnies = set()

has_won = False

for row in range(n):
    lair.append(list(input()))
    for col in range(m):
        if lair[row][col] == "P":
            p_row, p_col = row, col
            lair[row][col] = "."
        elif lair[row][col] == "B":
            bunnies.add((row, col))

commands = input()

MOVES = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

for command in commands:
    direction_row, direction_col = MOVES[command]
    new_p_row, new_p_col = p_row + direction_row, p_col + direction_col

    spread_bunnies(lair, bunnies)

    if not (0 <= new_p_row < n and 0 <= new_p_col < m):
        has_won = True
        break

    p_row, p_col = new_p_row, new_p_col
    if lair[p_row][p_col] == "B":
        break

[print("".join(row)) for row in lair]
print(f"{'won' if has_won else 'dead'}: {p_row} {p_col}")

