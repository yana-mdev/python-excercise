rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total = 0

for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)
    total += sum(elements)

    
print(total)
print(matrix)