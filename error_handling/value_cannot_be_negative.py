class ValueCannotBeNegative(Exception):
    pass


for num in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
