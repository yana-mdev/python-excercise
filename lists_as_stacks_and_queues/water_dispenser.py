from collections import deque

quantity = int(input())
people = deque()

while True:
    name = input()
    if name == "Start":
        break
    people.append(name)

while True:
    command = input()
    if command == "End":
        break
    parted = command.split()
    if command.isdigit():
        liters = int(command)
        if quantity >= liters:
            print(f"{people.popleft()} got water")
            quantity -= liters
        else:
            print(f"{people.popleft()} must wait")
    elif parted[0] == "refill":
        liters = int(parted[1])
        quantity += liters

print(f"{quantity} liters left")