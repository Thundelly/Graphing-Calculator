

class Equation:
    """
    Encapsulates equations. Each equation will know its own notation.
    """
    def __init__(self, equation: str, notation: str):
        """
        Constructor
        """
        self.equation = None
        self.notation = None

        self.set_equation(equation)

        if notation == "prefix" or notation == "infix" or notation == "postfix":
            self.notation = notation

        else:
            raise Exception("Invalid equation notation. Valid notations are: 'prefix', 'infix', or 'postfix'. \
                            Current notation: {}.".format(notation))

    def set_equation(self, equation: str) -> None:
        """
        Modifies equation
        :param equation: Assigns equation string
        :return: None
        """
        self.equation = equation

    def get_equation(self) -> str:
        """
        Returns the equation itself
        :return: equation
        """
        return self.equation

    def get_notation(self) -> str:
        """
        Returns the notation mode
        :return: notation
        """
        return self.notation
