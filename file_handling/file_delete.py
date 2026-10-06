import os

path = "files/my_first_file.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("File already deleted!")

# if os.path.exists(path):
#    os.remove(path)
# else:
#    print("File already deleted!")
