def print_row(size, row):
    print(" " * (size - row) + "* " * row)

def print_up(size):
    for row in range(1, size):
        print_row(size, row)


def print_down(size):
    for row in range(size, 0, -1):
        print_row(size, row)


def rhombus_of_stars(size):
    print_up(size)
    print_down(size)

number = int(input())
rhombus_of_stars(number)