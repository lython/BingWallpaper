#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4 import QtGui
from theme_qss import Theme

class BarBottom(QtGui.QFrame):
    def __init__(self, parent=None):
        super(BarBottom, self).__init__()

        self.setMaximumHeight(100)
        self.setStyleSheet(Theme().Theme)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = BarBottom()
    mainWin.show()
    sys.exit(app.exec_())