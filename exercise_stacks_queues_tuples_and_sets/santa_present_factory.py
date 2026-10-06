from collections import deque

crafting_toys_materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

points = {
    150:"Doll",
    250:"Wooden train",
    300:"Teddy bear",
    400:"Bicycle"
}

presents = { }

while crafting_toys_materials and magic_level:
    total_magic_level = crafting_toys_materials[-1] * magic_level[0]
    if total_magic_level in points:
        present_name = points[total_magic_level]
        presents[present_name] = presents.get(present_name, 0) + 1
        crafting_toys_materials.pop()
        magic_level.popleft()
    elif total_magic_level < 0:
        crafting_toys_materials.append(crafting_toys_materials.pop() + magic_level.popleft())
    elif total_magic_level > 0:
        magic_level.popleft()
        crafting_toys_materials[-1] += 15
    else:
        if crafting_toys_materials[-1] == 0:
            crafting_toys_materials.pop()
        if magic_level[0] == 0:
            magic_level.popleft()


if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if crafting_toys_materials:
    print(f"Materials left: {', '.join(map(str, reversed(crafting_toys_materials)))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")