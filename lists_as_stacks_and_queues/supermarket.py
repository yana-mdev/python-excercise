from collections import deque
customer_queue = deque()
while True:
    command = input()
    if command == "End":
        break
    elif command == "Paid":
        for _ in range(len(customer_queue)):
            print(customer_queue.popleft())
    else:
        customer_queue.append(command)

print(f"{len(customer_queue)} people remaining.")
