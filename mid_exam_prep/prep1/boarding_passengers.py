def boarding_passengers(capacity, *args):
    benefits_program = {}
    total_passengers = sum(num for num, _ in args)
    boarded_passengers = 0

    for element in args:
        num_of_passengers, name = element
        num_of_passengers = int(num_of_passengers)
        if capacity == 0:
            break

        if capacity >= num_of_passengers:
            benefits_program[name] = (benefits_program.get(name, 0) + num_of_passengers)
            capacity -= num_of_passengers
            boarded_passengers += num_of_passengers

    result = sorted(benefits_program.items(), key=lambda x: (-x[1], x[0]))

    output = "Boarding details by benefit plan:\n"

    for name, guests in result:
        output += f"## {name}: {guests} guests\n"

    if boarded_passengers == total_passengers:
        output += "All passengers are successfully boarded!"
    elif capacity == 0:
        output += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        output += f"Partial boarding completed. Available capacity: {capacity}."

    return output


