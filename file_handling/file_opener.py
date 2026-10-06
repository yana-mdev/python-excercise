import os
from random.constants import path_to_dir

path = os.path.join(path_to_dir, "advanced", "file_handling", "files/text.txt")

try:
    file = open(path)
    print("File found")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")



