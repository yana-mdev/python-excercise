from collections import deque

quantity_of_food = int(input())
orders = deque(map(int, input().split()))

biggest_order = max(orders)
print(biggest_order)

while orders and orders[0] <= quantity_of_food:
    quantity_of_food -= orders.popleft()

if not orders:
    print("Orders complete")
else:
    print(f"Orders left:", *orders)