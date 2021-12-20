from AdventOfCode.AdventData import AdventData


def day2_part1(dataset):
    """
    Multiplies the vertical position with horizontal position
    with forward adding forward value
    down adding down value
    up susbtracting down value
    Args:
        dataset: A list containing the data

    Returns: forward position x down position

    """
    forward = 0
    down = 0
    for i in dataset:
        current_entry = i.split()
        if current_entry[0] == "forward":
            forward += int(current_entry[1])
        elif current_entry[0] == "down":
            down += int(current_entry[1])
        elif current_entry[0] == "up":
            down -= int(current_entry[1])
    return forward*down


def day2_part2(dataset):
    """
    Multiplies the vertical position with horizontal position
    with down adding aim value
    up substracting aim value
    forward adding forward value while adding aim*value to down
    Args:
        dataset: A list containing the data

    Returns: forwrd value x down value

    """
    forward = 0
    down = 0
    aim = 0
    for i in dataset:
        current_entry = i.split()
        if current_entry[0] == "forward":
            forward += int(current_entry[1])
            down += (aim*int(current_entry[1]))
        elif current_entry[0] == "down":
            aim += int(current_entry[1])
        elif current_entry[0] == "up":
            aim -= int(current_entry[1])
    return forward * down


day = AdventData(2, "Day2.txt")
data = day.get_data()

print(day2_part1(data))
print(day2_part2(data))
