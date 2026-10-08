from modules.fibonacci_sequence.core import create_sequence, locate


sequence = None

while True:
    command = input()

    if command == "Stop":
        break

    num = int(command.split()[-1])

    if command.startswith("Create"):
        sequence = create_sequence(num)
        print(*sequence)

    elif command.startswith("Locate"):
        if sequence:
            print(locate(num, sequence))
        else:
            print("Please first initialize a sequence")

