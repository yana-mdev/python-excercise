from collections import deque

n = int(input())
commands = deque(input().split())

matrix = []
miner_row, miner_col = 0, 0
coal = 0
collected_coal = 0
end_game = False

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "s":
            miner_row, miner_col = row, col
        if matrix[row][col] == "c":
            coal += 1


MINER_MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while commands:
    curr_command = commands.popleft()
    dr, dc = MINER_MOVES[curr_command]
    new_row, new_col = miner_row + dr, miner_col + dc

    if not (0 <= new_row < n and 0 <= new_col < n):
        continue

    if matrix[new_row][new_col] == "e":
        print(f"Game over! ({new_row}, {new_col})")
        end_game = True
        break

    if matrix[new_row][new_col] == "c":
        collected_coal += 1
        matrix[new_row][new_col] = "*"
        if collected_coal == coal:
            print(f"You collected all coal! ({new_row}, {new_col})")
            end_game = True
            break

    miner_row, miner_col = new_row, new_col


if not end_game:
    print(f"{coal - collected_coal} pieces of coal left. ({miner_row}, {miner_col})")
