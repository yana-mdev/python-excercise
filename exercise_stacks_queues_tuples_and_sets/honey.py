from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(str(x) for x in input().split())

operators = {
    "+": lambda x, y: abs(x + y),
    "*": lambda x, y: abs(x * y),
    "-": lambda x, y: abs(x - y),
    "/": lambda x, y: abs(x / y) if y != 0 else 0,
}

total_honey_made = 0

while nectar and working_bees and operators:
    current_bee = working_bees[0]
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        result = operators[current_symbol](current_bee, current_nectar)
        total_honey_made += result
        working_bees.popleft()
    else:
        continue


print(f"Total honey made: {total_honey_made}")
if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")