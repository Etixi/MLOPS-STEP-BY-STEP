class MathOperation:
    """
    Performs basic math operations.

    Attributes:
    ----------
    num : int or float
        The input number for the operations.
    """

    def __init__(self, num: int) -> None:
        """
        Initializes the MathOperation class with the given number.

        Parameters:
        -----------
        num : int or float
            The input number for the operations.
        """
        self.num = num

    def add_two(self) -> int:
        """
        Adds 2 to the number.

        Returns:
        --------
        int
            The result after adding 2 to the number.
        """
        return self.num + 2

    def multiply_by_three(self) -> int:
        """
        Multiplies the number by 3.

        Returns:
        --------
        int
            The result after multiplying the number by 3.
        """
        return self.num * 3

