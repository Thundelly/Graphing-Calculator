import re
from model.equation import Equation
from model.token import Token


class Tokenizer:
    """
    Takes the Equation object and breaks it down to list
    of Tokens.

    Input: Equation
    Output: List of Tokens
    """
    @staticmethod
    def tokenize(equation_input: Equation) -> list:
        """
        Breaks down the Equation object into a list
        of Tokens.
        :return: List of Tokens.
        """
        equation = equation_input.get_equation()
        tokens = []

        pattern = re.compile(r"([+*/()-^])")                 # regex for delimiters
        equation = pattern.sub(" \\1 ", equation).split() # split with whitespace delimiter

        for elem in equation:
            token = Token(elem)
            tokens.append(token)

        return tokens

    @property
    def untokenize(self) -> Equation:
        """
        Takes the list of Tokens and returns a string
        equation corresponding to the list.
        :return: Equation object.
        """
        raise NotImplementedError("Implement this function later!")

