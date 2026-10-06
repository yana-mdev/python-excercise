def is_valid_position(row1_, col1_, row2_, col2_, rows_, cols_):
    return 0 <= row1_ < rows_ and 0 <= row2_ < rows_ and 0 <= col1_ < cols_ and 0 <= col2_ < cols_


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = map(int, command[1:])
        if is_valid_position(row1, col1, row2, col2, rows, cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2],  matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
        continue

