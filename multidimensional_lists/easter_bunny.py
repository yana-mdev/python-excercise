rows = int(input())

matrix = []
bunny_r, bunny_c = 0, 0

for row in range(rows):
    line = input().split()
    if "B" in line:
        bunny_r, bunny_c = row, line.index("B")
    matrix.append(line)

BUNNY_MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_eggs = -float("inf")
best_direction = ""
best_path = []

for direction, (d_r, d_c) in BUNNY_MOVES.items():
    eggs = 0
    curr_path = []

    r, c = bunny_r + d_r, bunny_c + d_c

    while 0 <= r < rows and 0 <= c < len(matrix[0]):
        if matrix[r][c] == "X":
            break

        eggs += int(matrix[r][c])
        curr_path.append([r, c])

        r += d_r
        c += d_c

    if eggs > max_eggs and curr_path:
        max_eggs = eggs
        best_direction = direction
        best_path = curr_path

print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)