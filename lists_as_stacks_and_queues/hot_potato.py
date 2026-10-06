from collections import deque
kids = deque(input().split())
toss = int(input())

while len(kids) > 1:
    kids.rotate(1 - toss)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")