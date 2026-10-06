rows, columns = map(int, input().split(", "))
matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for j in range(columns):
    result = 0
    for i in range(rows):
        result += matrix[i][j]
    print(result)
