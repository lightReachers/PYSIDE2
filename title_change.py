import sys
from PySide2.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.ledText = QLineEdit("This is line edit", self)
        self.ledText.move(50, 50)

        self.btnUpdate = QPushButton("Update Window Title", self)
        self.btnUpdate.move(50, 80)

        self.btnUpdate.clicked.connect(self.evt_update_title)

    def evt_update_title(self):
        self.setWindowTitle(self.ledText.text())


def main():
    app = QApplication(sys.argv)
    win = DlgMain()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()