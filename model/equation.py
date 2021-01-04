

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

        if notation == "prefix":
            self.set_notation_to_prefix()
        elif notation == "infix":
            self.set_notation_to_infix()
        elif notation == "postfix":
            self.set_notation_to_postfix()
        else:
            self.notation = notation
            raise Exception("Invalid equation notation. Valid notations are: 'prefix', 'infix', or 'postfix'. "
                            "Current notation: {}.".format(notation))

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

    def set_notation_to_prefix(self) -> None:
        """
        Set notation to prefix
        :return: None
        """
        self.notation = "prefix"

    def set_notation_to_infix(self) -> None:
        """
        Set notation to infix
        :return: None
        """
        self.notation = "infix"

    def set_notation_to_postfix(self) -> None:
        """
        Set notation to postfix
        :return: None
        """
        self.notation = "postfix"

    def get_notation(self) -> str:
        """
        Returns the notation mode
        :return: notation
        """
        return self.notation
