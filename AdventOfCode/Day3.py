from AdventOfCode.AdventData import AdventData


def find_greater_occurence(list_data, index):
    """

    Args:
        list_data: list containing data to analyse
        index: index of each data to count

    Returns:
        a string containing either "1" or "0", the most frequent at that index
    """

    count = 0
    for i in list_data:
        if i[index] == "1":
            count += 1
        elif i[index] == "0":
            count -= 1
    if count >= 0:
        return str("1")
    else:
        return str("0")


def find_lesser_occurence(list_data, index):
    """

    Args:
        list_data: list containing data to analyse
        index: index of each data to count

    Returns:
        a string containing either "1" or "0", the less frequent at that index
    """

    count = 0
    for i in list_data:
        if i[index] == "1":
            count += 1
        elif i[index] == "0":
            count -= 1
    if count >= 0:
        return str("0")
    else:
        return str("1")


def remove_item_from_list(list_data, value, index):
    """

    Args:
        list_data: List containing the data to remove
        value: either "1" or "0"
        index: index to compare with value

    Returns:
        None
    """
    if len(list_data) > 1:
        for i in list(list_data):
            if str(value) == str(i[index]):
                list_data.remove(i)


def convert_binary_to_decimal(binary, number_of_bits):
    """

    Args:
        binary: the number in binary
        number_of_bits: number of bits

    Returns:
        decimal value of the number
    """
    decimal = 0
    bit_value = number_of_bits-1
    for i in range(number_of_bits):
        if binary[i] == str("1"):
            decimal += (2**bit_value)
        bit_value -= 1
    return decimal


def day3_part1(dataset):
    gamma_binary = ""
    epsilon_binary = ""
    for bit in range(12):
        value_gamma = find_greater_occurence(dataset, bit)
        value_epsilon = find_lesser_occurence(dataset, bit)
        gamma_binary = gamma_binary + str(value_gamma)
        epsilon_binary = epsilon_binary + str(value_epsilon)
    gamma_decimal = int(convert_binary_to_decimal(gamma_binary, 12))
    epsilon_decimal = int(convert_binary_to_decimal(epsilon_binary, 12))
    return gamma_decimal * epsilon_decimal


def day3_part2(oxygen, co2):
    for bit in range(12):
        value_oxygen = find_lesser_occurence(oxygen, bit)
        value_co2 = find_greater_occurence(co2, bit)
        remove_item_from_list(oxygen, value_oxygen, bit)
        remove_item_from_list(co2, value_co2, bit)
    oxygen_binary = str(oxygen[0])
    co2_binary = str(co2[0])
    oxygen_decimal = int(convert_binary_to_decimal(oxygen_binary, 12))
    co2_decimal = int(convert_binary_to_decimal(co2_binary, 12))
    return oxygen_decimal * co2_decimal


day = AdventData(3, "Day3.txt")
data = day.get_data()
oxygen_list = list(data)
co2_list = list(data)
print(day3_part1(data))
print(day3_part2(oxygen_list, co2_list))
