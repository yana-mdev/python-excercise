stack = []
n = int(input())

for _ in range(n):
    query = input().split()
    if query[0] == "1":
        number = int(query[1])
        stack.append(number)
    elif query[0] == "2" and stack:
        stack.pop()
    elif query[0] == "3":
        if stack:
            print(max(stack))
    elif query[0] == "4":
        if stack:
            print(min(stack))

print(", ".join(map(str, reversed(stack))))