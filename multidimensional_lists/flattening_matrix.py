rows = int(input())

flattening_matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    for element in elements:
        flattening_matrix.append(element)

print(flattening_matrix)