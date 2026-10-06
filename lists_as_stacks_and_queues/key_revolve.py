from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

reloading = 0
bullets_count = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    reloading += 1
    bullets_count += 1

    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if reloading == gun_barrel_size and bullets:
        print("Reloading!")
        reloading = 0

if not locks:
    money_earned = intelligence_value - (bullet_price * bullets_count)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")