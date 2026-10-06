from collections import deque

robots_data = input().split(";")
robots = []

for robot in robots_data:
    name, process_time = robot.split("-")
    robots.append({
        "name": name,
        "process_time": int(process_time),
        "free_at": 0
    })

hours, minutes, seconds = [int(x) for x in input().split(":")]
start_time = hours * 3600 + minutes * 60 + seconds
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

current_time = start_time

while products:
    current_time += 1
    curr_product = products.popleft()

    for r in robots:
        if r["free_at"] <= current_time:
            r["free_at"] = current_time + r["process_time"]
            h = current_time // 3600
            m = (current_time % 3600) // 60
            s = (current_time % 3600) % 60
            h %= 24
            print(f"{r['name']} - {curr_product} [{h:02d}:{m:02d}:{s:02d}]")
            break
    else:
        products.append(curr_product)


