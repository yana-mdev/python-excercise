n, m = map(int, input().split())

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print(*first_set & second_set, sep="\n")