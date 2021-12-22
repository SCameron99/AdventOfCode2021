from AdventOfCode.AdventData import AdventData


class Cell:
    """
    Bingo Cell Class
    """
    def __init__(self, number, position):
        """

        Args:
            number: The number on that Bingo Cell
        """
        self.number = number
        self.position = position
        self.marked = False


class BingoCard:
    """
    Bingo Card Class
    """
    def __init__(self, cell_list):
        """

        Args:
            cell_list: a list of 15 cells
        """
        self.cell_list = cell_list
        self.win = False


def create_bingo_cards(dataset):
    """
    Creates a list of bingo cards containing 25 cells
    Args:
        dataset: a list containing the numbers on bingo cards, 5 per line, 5 lines per cards

    Returns: a list of BingoCard objects

    """
    card_list = []
    cell_list = []
    cell_position = 1
    for i in dataset:
        cells = i.split()
        if len(cells) == 5:
            for j in cells:
                cell = Cell(j, cell_position)
                cell_list.append(cell)
                cell_position += 1
                if len(cell_list) == 25:
                    card = BingoCard(cell_list)
                    card_list.append(card)
                    cell_list = []
                    cell_position = 1
    return card_list


def mark_cell(card_list, number):
    """
    set the attribute of every cell in every card of card_list to True if the cell number is the number parameter
    Args:
        card_list: list of BingoCard objects
        number: the number to mark

    Returns: None

    """
    for card in card_list:
        for cell in card.cell_list:
            if int(cell.number) == int(number):
                cell.marked = True
    return None


def check_bingo():
    """
    checks throught the card list if a vertical or horizontal line is complete
    Returns: the first winning card in the list
            if no cards wins, returns None

    """
    for card in cards:
        possible_win = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23],
                        [4, 9, 14, 19, 24], [5, 10, 15, 20, 25]]
        checked = []
        for cell in card.cell_list:
            if cell.marked:
                checked.append(cell.position)
        for line in range(10):
            bingo = all(elem in checked for elem in possible_win[line])
            if bingo:
                card.win = True
                return card
    return None


def day4_part1(dataset):
    for i in dataset:
        numbers = i.split(",")
        if len(numbers) > 5:
            for number in numbers:
                mark_cell(cards, number)
                winner = check_bingo()
                if winner:
                    unmarked_sum = 0
                    for cell in winner.cell_list:
                        if not cell.marked:
                            unmarked_sum += int(cell.number)
                    return unmarked_sum * int(number)


def day4_part2(dataset):
    for i in dataset:
        numbers = i.split(",")
        if len(numbers) > 5:
            for number in numbers:
                mark_cell(cards, number)
                winner = check_bingo()
                while winner:
                    if len(cards) > 1:
                        cards.remove(winner)
                        winner = check_bingo()
                    else:
                        unmarked_sum = 0
                        for cell in winner.cell_list:
                            if not cell.marked:
                                unmarked_sum += int(cell.number)
                        return unmarked_sum * int(number)


day = AdventData(4, "Day4.txt")
data = day.get_data()
cards = create_bingo_cards(data)
print(day4_part1(data))
print(day4_part2(data))
