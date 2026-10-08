from math import log


num = int(input())

try:
    log_base = int(input())
    print(f"{log(num, log_base):.2f}")
except ValueError:
    print(f"{log(num):.2f}")



