expression = input()

parentheses_stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses_stack.append(i)
    elif expression[i] == ")":
        start_index = parentheses_stack.pop()
        end_index = i + 1
        print(expression[start_index:end_index])