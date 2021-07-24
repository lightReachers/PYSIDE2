import sys
from PySide2.QtWidgets import *


class DlgMain(QWidget):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setWindowTitle("MSG box example")
        self.resize(200, 200)

        self.btn = QPushButton('ShowMSG', self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        res = QMessageBox.question(self, "Disk Full", "Your Disk is almost full")
        if res == QMessageBox.Yes:
            QMessageBox.information(self, "", "You clicked YES!!")
        else:

            QMessageBox.information(self, "", "Tou clicked No!!")


def main():
    app = QApplication(sys.argv)
    win = DlgMain()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
