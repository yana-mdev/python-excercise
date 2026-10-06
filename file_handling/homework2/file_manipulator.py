import os

while True:
    command = input()
    if command == "End":
        break

    action, file_name, *args = command.split("-")
    path = os.path.join("files", file_name)

    if action == "Create":
        open(path, "w").close()
    elif action == "Add":
        content = args
        with open(path, "a") as file:
            file.write(f"{content}\n")
    elif action == "Replace":
        old_string, new_string = args
        try:
            with open(path, "r+") as file:
                file_content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(file_content.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(path)
        except FileNotFoundError:
            print("An error occurred")

