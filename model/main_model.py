from model.equation import Equation
from model.converter import Converter


class Main_Model:
    def __init__(self):
        converter = Converter()
        equation_input = Equation("1+2*3/(4-5)", "infix")

        equation_output = converter.convert_infix_to_postfix(equation_input)

        print("Infix Notation:", equation_input.get_equation())
        print("Postfix Notation:", equation_output.get_equation())
