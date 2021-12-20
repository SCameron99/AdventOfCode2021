from AdventOfCode.AdventData import AdventData


def day1_part1(dataset):
    """
    Counts the number of time a value is greater than the previous.
    Args:
        dataset: A list containing the data

    Returns: The number of times a value is greater than the previous

    """
    count = 0
    previous = -1
    for i in dataset:
        current = int(i)
        if previous == -1:
            previous = current
        else:
            if current > previous:
                count += 1
            previous = current
    return count


def day1_part2(dataset):
    """
    Compares 3 values with the 3 next values (Including the 2nd and third from the first set) and returns the number
    of times the second set is greater.
    Args:
        dataset: A list containing the data

    Returns: The number of times the second set is greater tahn the first

    """
    count = 0
    a = -1
    b = -1
    c = -1
    for i in dataset:
        d = int(i)
        if a == -1:
            a = b
            b = c
            c = d
        else:
            if (d + c + b) > (c + b + a):
                count += 1
            a = b
            b = c
            c = d
    return count


day = AdventData(1, "Day1.txt")
data = day.get_data()
print(day1_part1(data))
print(day1_part2(data))
