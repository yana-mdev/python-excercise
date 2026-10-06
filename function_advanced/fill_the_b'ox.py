def fill_the_box(height, length, width, *args):
    box_volume = height*length*width
    cubes = 0
    for item in args:
        if item == "Finish":
            break
        cubes += item

    if box_volume > cubes:
        return f"There is free space in the box. You could put {box_volume-cubes} more cubes."

    return f"No more free space! You have {cubes-box_volume} more cubes."

