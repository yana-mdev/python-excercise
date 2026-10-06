def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [int(x) for x in args[:-1] if x % 2 == 0]
    return [int(x) for x in args[:-1] if x % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))