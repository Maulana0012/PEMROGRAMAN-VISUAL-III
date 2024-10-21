import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Form_Input import Ui_Form_Input
import Form_ShowData
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = Ui_Form_Input()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())