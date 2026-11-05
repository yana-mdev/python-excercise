from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())

total_weight = 0

while packages and couriers:
    current_courier = couriers.popleft()
    current_package = packages.pop()

    if current_courier >= current_package:
        total_weight += current_package
        courier_remaining_capacity = current_courier - (current_package * 2)
        if courier_remaining_capacity > 0:
            couriers.append(courier_remaining_capacity)
    else:
        total_weight += current_courier
        packages.append(current_package - current_courier)


print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")