first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}


for _ in range(int(input())):
    command = input().split()
    numbers = [int(x) for x in command[2:]]
    if command[0] == "Add":
        if command[1] == "First":
            first_sequence.update(numbers)
        elif command[1] == "Second":
            second_sequence.update(numbers)
    elif command[0] == "Remove":
        if command[1] == "First":
            first_sequence.difference_update(numbers)
        elif command[1] == "Second":
            second_sequence.difference_update(numbers)
    elif command[0] == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")