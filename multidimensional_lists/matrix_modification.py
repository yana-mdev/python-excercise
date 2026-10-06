rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    action = command.split()[0]
    row, col, value = map(int, command.split()[1:])
    if not (0 <= row < rows and 0 <= col < rows):
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row)
