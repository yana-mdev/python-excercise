import os
from random.constants import path_to_dir

path = os.path.join(path_to_dir, "advanced", "file_handling", "files", "numbers.txt")
file = open(path)

# numbers = [int(x) for x in file.read().split("\n") if x]
# print(sum(numbers))

# or

total = 0
for number in file:
    total += int(number)
print(total)