from string import punctuation

with open("files/ex2_input.txt") as input_file, open("files/ex2_output.txt", "w") as output_file:
    for row, line in enumerate(input_file, start=1):
        letters = 0
        punctuation_marks = 0
        for ch in line:
            if ch.isalpha():
                letters += 1
            elif ch in punctuation:
                punctuation_marks += 1
        output_file.write(f"Line {row}: {line.strip()} ({letters})({punctuation_marks})\n")
