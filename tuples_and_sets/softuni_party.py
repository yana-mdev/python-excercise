n = int(input())
reservations = set()

for _ in range(n):
    reservation_code = input()
    reservations.add(reservation_code)

while True:
    reservation = input()
    if reservation == "END":
        break
    if reservation in reservations:
        reservations.remove(reservation)


print(len(reservations))
sorted_reservations = sorted(reservations)
print("\n".join(sorted_reservations))