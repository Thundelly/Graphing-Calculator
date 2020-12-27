from PySide6.QtWidgets import QApplication
from view.main_window import Main_Window
import sys


class Graphing_Calculator:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Main_Window()

    def run(self):
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    graphing_calculator = Graphing_Calculator()
    graphing_calculator.run()
