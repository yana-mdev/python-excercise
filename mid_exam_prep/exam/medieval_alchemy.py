from collections import deque


POTIONS = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength",
}

crafted_potions = []

substance_quantities = [int(x) for x in input().split(", ")]
crystal_energy_level = deque(int(x) for x in input().split(", "))

while substance_quantities and crystal_energy_level and len(crafted_potions) < 5:
    curr_substance = substance_quantities.pop()
    curr_energy = crystal_energy_level.popleft()
    sum_elements = curr_substance + curr_energy

    if sum_elements in POTIONS and POTIONS[sum_elements] not in crafted_potions:
        crafted_potions.append(POTIONS[sum_elements])
    else:
        possible_potions = [energy for energy in POTIONS if energy < sum_elements
                            and POTIONS[energy] not in crafted_potions]
        if possible_potions:
            max_potion = max(possible_potions)
            crafted_potions.append(POTIONS[max_potion])
            curr_energy -= 20
        else:
            curr_energy -= 5

        if curr_energy > 0:
            crystal_energy_level.append(curr_energy)



if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")


if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substance_quantities:
    print(f"Substances: {', '.join(map(str, reversed(substance_quantities)))}")

if crystal_energy_level:
    print(f"Crystals: {', '.join(map(str, crystal_energy_level))}")




