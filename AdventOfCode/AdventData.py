"""
AdventData Module
"""


class AdventData:
    """
    Class for a dataset of the Advent Of Code

    Attributes:
        day: day of the code challenge
        text_file (list): list containing the data
    """

    def __init__(self, day, text_file):
        """
        AdventData class constructor
        Args:
            day: day of the code challenge
            text_file (.txt file): initial value of data
        """
        self.day = day
        self.text_file = text_file

    def get_data(self):
        """
        method converting .txt file to list
        """
        data = []
        file = open(self.text_file, mode="r", encoding="utf-8")
        for i in file:
            j = i.strip("\n")
            data.append(j)
        file.close()
        return data
