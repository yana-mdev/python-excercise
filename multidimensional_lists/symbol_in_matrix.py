n = int(input())
matrix = []
found = False

for _ in range(n):
    row = [x for x in input()]
    matrix.append(row)

symbol = input()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
