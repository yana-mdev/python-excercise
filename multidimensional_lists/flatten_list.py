strings = input().split("|")

matrix = []

for i in range(len(strings) - 1, -1, -1):
    line = strings[i].split()
    if line:
        matrix.append(line)

for row in matrix:
    print(*row, end=" ")