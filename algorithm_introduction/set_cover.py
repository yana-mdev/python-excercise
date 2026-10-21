def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_subsets = []
    remaining_set = sets.copy()

    while universe_set and remaining_set:
        best_set = max(remaining_set, key=lambda x: len(universe_set.intersection(x)))
        if not universe_set.intersection(best_set):
            break

        chosen_subsets.append(best_set)
        universe_set -= set(best_set)
        remaining_set.remove(best_set)

    if universe_set:
        return None
    return chosen_subsets



uni_set = [int(x) for x in input().split(", ")]
number_of_sets = int(input())

subsets = []

for _ in range(number_of_sets):
    new_set = [int(x) for x in input().split(", ")]
    subsets.append(new_set)


result = set_cover(uni_set, subsets)

if result is None:
    print("No solution exists")
else:
    for i in range(len(result)):
        result[i] = sorted(result[i])

    print(f"\nSets to take ({len(result)}): ")
    for s in result:
        print("{", ", ".join(map(str, s)), "}")