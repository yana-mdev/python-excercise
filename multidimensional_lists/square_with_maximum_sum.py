rows, columns = map(int, input().split(", "))
matrix = []

submatrix = []
biggest_sum = 0

for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]
        sum_element = current_element + next_element + element_below + element_diagonal
        if sum_element > biggest_sum:
            biggest_sum = sum_element
            submatrix = [[current_element, next_element], [element_below, element_diagonal]]

print(*submatrix[0])
print(*submatrix[1])
print(biggest_sum)