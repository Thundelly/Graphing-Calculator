

class Token:
    """
    Tokens that are used to store each number or operator
    in the equation. This token is later pushed into a
    stack of operators for RPN.

    Each token will know whether itself is an operator or
    a number.
    """
    def __init__(self, value):
        """
        Constructor
        :param value: Value of the token. This can either
        be an operator or a number.
        """
        self.precedence = None
        self.value = value

        self.operator = None

        self.set_precedence(value)

    def set_precedence(self, value):
        """
        Sets precedence of the operator.
        :param value: Value given to the token.
        :return:
        """
        precedences = {
            "^": 3,
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1,
            "(": 0,
            ")": 0
        }

        # Try to find the precedence for the key.
        # If found, assign the corresponding precendence
        # and set isOperator variable value to True
        try:
            self.precedence = precedences[value]
            self.operator = True

        # If the key was not found in the dictionary,
        # KeyError exception will be thrown. Take care
        # of this exception accordingly.
        except KeyError:
            self.precedence = 0
            self.operator = False

    def get_precedence(self):
        """
        Get precedence of the token.
        :return: Precedence of the token.
        """
        return self.precedence

    def get_value(self):
        """
        Get value of the token.
        :return: Value of the token.
        """
        return self.value

    def is_operator(self):
        return self.operator
