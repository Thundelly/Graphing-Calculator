from model.equation import Equation
from model.tokenizer import Tokenizer
from model.stack import Stack


class Converter:
    """
    Converts equations from one notation to another.
    Notations are: prefix, infix, and postfix.
    """

    def __init__(self):
        self.debug = True

    def convert_infix_to_postfix(self, equation_input: Equation) -> Equation:
        """
        Converts an infix (str) equation to a postfix (str) equation.
        :param equation_input: Equation object of infix notation.
        :return: Equation object of postfix notation.
        """
        stack = Stack()
        output_str = ""

        if equation_input.get_notation() == "infix":
            tokenizer = Tokenizer()

            tokens_infix = tokenizer.tokenize(equation_input)

            # Scan infix notation from left to right.
            for token in tokens_infix:

                if self.debug:
                    print("Output String:", output_str)
                    print("Operator Stack:", stack)
                # If the token is a number, add to output string.
                if not token.is_operator():
                    output_str += token.get_value()
                # If left parenthesis is found, push to stack.
                elif token.get_value() == "(":
                    stack.push(token)
                # If right parenthesis is found.
                elif token.get_value() == ")":
                    # Pop from stack and add to output string
                    # until left parenthesis is found.
                    while (not stack.is_empty()) and stack.top().get_value() != "(":
                        popped = stack.pop()
                        output_str += popped.get_value()
                    # Make sure the left parenthesis is no longer
                    # in the stack. If not found, break out of
                    # conditional statement.
                    if (not stack.is_empty()) and stack.top().get_value() != "(":
                        break
                    # If the left parenthesis is found, pop it from
                    # the stack.
                    else:
                        stack.pop()
                # Operator was found
                else:
                    # Pop from the stack and compare with currently scanned token
                    # until popped operator has lower precedence as the
                    # currently scanned token, continue popping.
                    # At the end, push the currently scanned token back to the stack.
                    while (not stack.is_empty()) and (stack.top().get_precedence() >= token.get_precedence()):
                        output_str += stack.pop().get_value()
                    stack.push(token)
            # pop from the stack until it is empty
            # and add the operators to the output string
            while not stack.is_empty():
                output_str += stack.pop().get_value()

            # Create an equation object for the output string and return.
            return Equation(output_str, "postfix")

        # If the given equation is not infix, raise an exception.
        else:
            raise Exception("Incorrect notation input. Current input: {}.".format(equation_input.get_notation()))