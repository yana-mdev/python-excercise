parentheses = input()

parentheses_matches = {"(": ")", "{": "}", "[": "]"}

stack = []

for char in parentheses:
    if char in parentheses_matches:
        stack.append(char)
    elif char in parentheses_matches.values():
        if not stack:
            print("NO")
            break
        last_opening = stack.pop()
        if parentheses_matches[last_opening] != char:
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")
