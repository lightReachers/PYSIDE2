import sys
from PySide2.QtWidgets import *

print(sys.argv)
app = QApplication(sys.argv)

dlgMain = QWidget()
dlgMain.setWindowTitle("First GUI")
dlgMain.show()

sys.exit(app.exec_())