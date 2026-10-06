from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
passed = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{passed} total cars passed the crossroads.")
        break
    if command != "green":
        cars.append(command)
        continue
    current_time = green_light
    while cars and current_time > 0:
        current_car = cars.popleft()
        needed_time = len(current_car)
        if needed_time <= current_time + free_window:
            passed += 1
            current_time -= needed_time
        else:
            hit_index = current_time + free_window
            print("A crash happened!")
            print(f"{current_car} was hit at {current_car[hit_index]}.")
            exit()