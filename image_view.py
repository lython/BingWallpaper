#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4 import QtGui, QtCore, QtWebKit, Qt

class ImageView(QtWebKit.QWebView):
    def __init__(self):
        super(ImageView, self).__init__()

        self.pos_x = 0

    def mouseDoubleClickEvent(self, event):
        event.ignore()

    def mousePressEvent(self, event):
        event.ignore()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.pos_x = event.globalPos() - self.pos()

    def contextMenuEvent(self, event):
        event.ignore()

    def enterEvent(self, event):
        self.setCursor(Qt.Qt.PointingHandCursor)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = ImageView()
    mainWin.show()
    sys.exit(app.exec_())