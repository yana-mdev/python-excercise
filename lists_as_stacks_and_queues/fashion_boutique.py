clothes = list(map(int, input().split()))
capacity_of_rack = int(input())

racks = 1
current_rack = capacity_of_rack

while clothes:
    current = clothes.pop()
    if current <= current_rack:
        current_rack -= current
    else:
        racks += 1
        current_rack = capacity_of_rack - current

print(racks)



