file = open("files/my_first_file.txt", "w")

file.write('I just created my first file!')
file.close()

#or

with open("files/my_second_file.txt", "a") as file:
    file.write("new try")