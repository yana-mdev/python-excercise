import os

files = {}
directory = "files/ex4_directory"


def get_files(folder, level=float("inf")):
    if level < 0:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            _, ext = os.path.splitext(element)
            if ext:
                if ext not in files:
                    files[ext] = []
                files[ext].append(element)
        elif os.path.isdir(f):
            get_files(f, level - 1)


get_files(directory, 1)

with open(os.path.join(directory, "report.txt"), "w") as output:
    for extension, file_names in sorted(files.items()):
        output.write(f"{extension}\n")
        for file in sorted(file_names):
            output.write(f"- - - {file}\n")

