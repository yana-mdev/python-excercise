from collections import deque

n = int(input())
matrix = [[(int(x)) for x in input().split()] for _ in range(n)]

bombs = deque((int(x), int(y)) for x, y in (pair.split(",") for pair in input().split()))

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
)

while bombs:
    current_bomb = bombs.popleft()
    curr_bomb_row = current_bomb[0]
    curr_bomb_col = current_bomb[1]

    if matrix[curr_bomb_row][curr_bomb_col] <= 0:
        continue

    damage = matrix[curr_bomb_row][curr_bomb_col]
    for dr, dc in DIRECTIONS:
        new_row = curr_bomb_row + dr
        new_col = curr_bomb_col + dc
        if 0 <= new_row < n and 0 <= new_col < n:
            if matrix[new_row][new_col] > 0:
                matrix[new_row][new_col] -= damage

    matrix[curr_bomb_row][curr_bomb_col] = 0

alive_cells = 0
sum_of_cells = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            sum_of_cells += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")

for row in matrix:
    print(*row)
