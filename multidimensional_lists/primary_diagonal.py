n = int(input())
matrix = []
result = 0

for _ in range(n):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for i in range(n):
    result += matrix[i][i]

print(result)