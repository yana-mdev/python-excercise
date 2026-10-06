import os

files = {}
directory = "files/ex4_directory"

for element in os.listdir(directory):
    file = os.path.join(directory, element)
    if os.path.isfile(file):
        extension = element.split(".")[-1]
        if extension not in files:
            files[extension] = []
        files[extension].append(element)
    elif os.path.isdir(file):
        for el in os.listdir(file):
            filename = os.path.join(file, el)
            if os.path.isfile(filename):
                ext = el.split(".")[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open(os.path.join(directory, "report.txt"), "w") as output:
    for extension, file_names in sorted(files.items()):
        output.write(f".{extension}\n")
        for file in sorted(file_names):
            output.write(f"---{file}\n")


