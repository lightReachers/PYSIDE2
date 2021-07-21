import sys
from PySide2.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setWindowTitle("My GUI")
    # add more attributes and properties


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())