def recursive_factorial(number):
    if number == 1:
        return number

    return number * recursive_factorial(number - 1)


n = int(input())
print(recursive_factorial(n))