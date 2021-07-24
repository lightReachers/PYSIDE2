import sys
from PySide2.QtWidgets import *


class DlgMain(QWidget):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setWindowTitle("MSG box")
        self.resize(200, 200)

        self.btn = QPushButton('Get Text', self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        sName, bOK = QInputDialog.getText(self, "Txt", "Enter you name")
        if bOK:
            QMessageBox.information(self, "Name", "Your name is " + sName)
        else:
            QMessageBox.critical(self, "", "You cancel")


def main():
    app = QApplication(sys.argv)
    win = DlgMain()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
