from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

waste = 0

while cups and bottles:
    current_cup = cups[0]
    while current_cup > 0:
        current_bottle = bottles.pop()
        if current_bottle > current_cup:
            waste += (current_bottle - current_cup)
        current_cup -= current_bottle
    cups.popleft()

if cups:
    print(f"Cups:", *cups)
else:
    print(f"Bottles:", *reversed(bottles))

print(f"Wasted litters of water: {waste}")





