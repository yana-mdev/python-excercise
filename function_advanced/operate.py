from functools import reduce


def sum_nums(*args):
    return sum(args)


def sub_nums(*args):
    return reduce(lambda x, y: x - y, args)


def multi_nums(*args):
    return reduce(lambda x, y: x * y, args)


def div_nums(*args):
    return reduce(lambda x, y: x / y, args)


MAPPER = {
    "+": sum_nums,
    "-": sub_nums,
    "*": multi_nums,
    "/": div_nums
}


def operate(operator, *args):
    func = MAPPER[operator]
    return func(*args)
