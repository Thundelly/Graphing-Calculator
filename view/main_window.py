from PySide6.QtWidgets import QMainWindow


class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "Graphing Calculator V. 0.0.1"

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, 500, 500)
        self.show()
