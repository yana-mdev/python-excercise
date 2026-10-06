rows, columns = map(int, input().split())

matrix = [[x for x in input().split()] for _ in range(rows)]
square_matrix_count = 0

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]
        if current_element == next_element == element_diagonal == element_below:
            square_matrix_count += 1

print(square_matrix_count)