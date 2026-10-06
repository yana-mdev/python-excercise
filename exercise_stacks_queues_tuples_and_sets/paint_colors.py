from collections import deque

substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

collected_colors = []

while substrings:
    first_substring = substrings.popleft()
    last_substring = substrings.pop() if substrings else ""

    for color in (first_substring+last_substring, last_substring+first_substring):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        if len(first_substring) > 1:
            substrings.insert(len(substrings)//2, first_substring[:-1])
        if len(last_substring) > 1:
            substrings.insert(len(substrings)//2, last_substring[:-1])

valid_colors = []
for color in collected_colors:
    if color in main_colors:
        valid_colors.append(color)
    elif color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in collected_colors:
                break
        else:
            valid_colors.append(color)

print(valid_colors)