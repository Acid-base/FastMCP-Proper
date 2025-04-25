"""Module containing example classes and functions."""

from typing import List


class DataProcessor:
    """A class for processing data."""

    def __init__(self, data: List[int]) -> None:
        """Initializes the DataProcessor with a list of integers.

        Args:
            data: A list of integers to process.

        Raises:
            TypeError: If data is not a list.
            TypeError: If elements of data are not integers.
        """
        if not isinstance(data, list):
            raise TypeError("Data must be a list.")
        if not all(isinstance(x, int) for x in data):
            raise TypeError("All elements in data must be integers.")
        self.data = data

    def calculate_average(self) -> float:
        """Calculates the average of the data.

        Returns:
            The average value of the data.

        Raises:
            TypeError: if data is not a list of ints

        """
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)

    def find_max(self) -> int:
        """Finds the largest number in the data.

        Returns:
            The largest value of the data.

        Raises:
            ValueError: If the data list is empty.
        """
        if not self.data:
            raise ValueError("Data cannot be empty.")
        return max(self.data)


def greet(name: str) -> str:
    """Greets a person by name.

    Args:
      name: The person's name.
    Returns:
      A greeting string.

    Raises:
       TypeError: If name is not a string.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    message = f"Hello, {name}!"
    return message


def add(a: int, b: int) -> int:
    """Adds two integers.

    Args:
        a: The first integer.
        b: The second integer.
    Returns:
        The sum of the two integers.

    Raises:
       TypeError: If a or b is not an integer.
    """
    if not isinstance(a, int):
        raise TypeError("a must be an int")
    if not isinstance(b, int):
        raise TypeError("b must be an int")
    return a + b
