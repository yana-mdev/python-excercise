numbers = list(input().split())
new_numbers = []
for _ in range (len(numbers)):
    new_numbers.append(numbers.pop())

print(" ".join(new_numbers))