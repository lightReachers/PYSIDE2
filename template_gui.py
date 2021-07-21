import sys
from PySide2.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setWindowTitle("My GUI")

        self.ledTest = QLineEdit("This is QLineEdit", self)
        self.ledTest.move(50, 50)


def main():
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
