import sys
# from PyQt5.uic.properties import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(window)
window.show()
sys.exit(app.exec_())
