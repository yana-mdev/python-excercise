n = int(input())

matrix = []
alice_r, alice_c = 0, 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            alice_r, alice_c = row, col
            matrix[row][col] = "*"

ALICE_MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

collected_tea_bags = 0

while collected_tea_bags < 10:
    dr, dc = ALICE_MOVES[input()]
    r, c = alice_r + dr, alice_c + dc

    if not(0 <= r < n and 0 <= c < n):
        break

    curr_cell = matrix[r][c]
    matrix[r][c] = "*"
    alice_r, alice_c = r, c

    if curr_cell == "R":
        break

    if curr_cell.isdigit():
        collected_tea_bags += int(curr_cell)

if collected_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)