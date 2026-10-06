rows, cols = map(int, input().split())

start_letter = ord("a")

for row in range(rows):
    for col in range(cols):
        print(f"{chr(start_letter + row)}{chr(start_letter + row + col)}{chr(start_letter + row)}", end=" ")
    print()