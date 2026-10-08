from modules.math_operations.core import calculate

expression = input().split()


num1 = float(expression[0])
num2 = int(expression[2])
sign = expression[1]


print(f"{calculate(num1, num2, sign):.2f}")