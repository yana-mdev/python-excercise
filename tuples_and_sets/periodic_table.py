n = int(input())
unique_set = set()

for _ in range(n):
    chemical_compounds = set(input().split())
    unique_set.update(chemical_compounds)

print("\n".join(unique_set))

# or

new_set = set()
for el in range(int(input())):
    new_set = new_set.union(input().split())
print(*new_set, sep="\n")

# or shortest

print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")