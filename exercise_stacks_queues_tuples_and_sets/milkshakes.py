from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))
milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    current_chocolate = chocolates[-1]
    current_milk = cups_of_milk[0]

    if current_chocolate <= 0 or current_milk <= 0:
        if current_chocolate <= 0:
            chocolates.pop()
        if current_milk <= 0:
            cups_of_milk.popleft()
        continue

    if current_milk == current_chocolate:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print(f"Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print(f"Milk: empty")
