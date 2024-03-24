import sys
from PyQt5 import QtWidgets

from start import Main_AutoRecruit

app = QtWidgets.QApplication(sys.argv)
ui = Main_AutoRecruit()
ui.show()
sys.exit(app.exec_())
