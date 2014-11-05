#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4 import QtGui, Qt
from theme_qss import Theme
import os


class BarTop(QtGui.QFrame):
    def __init__(self, parent=None):
        super(BarTop, self).__init__()

        label_title = QtGui.QLabel(u"<font color=white size=10 face='微软雅黑'><b>必应壁纸</b></font>",self)
        #label_title.setAlignment(Qt.Qt.AlignCenter)

        self.btn_back = QtGui.QToolButton(self, icon=QtGui.QIcon("icon/appbar_back.png"))
        self.btn_back.setStyleSheet(Theme().RoundButton)
        self.btn_back.setIconSize(Qt.QSize(48, 48))
        self.btn_next = QtGui.QToolButton(self, icon=QtGui.QIcon("icon/appbar_next.png"))
        self.btn_next.setStyleSheet(Theme().RoundButton)
        self.btn_next.setIconSize(Qt.QSize(48, 48))
        self.btn_today = QtGui.QToolButton(self, icon=QtGui.QIcon("icon/appbar_today.png"))
        self.btn_today.setStyleSheet(Theme().RoundButton)
        self.btn_today.setIconSize(Qt.QSize(48, 48))
        self.btn_save = QtGui.QToolButton(self, icon=QtGui.QIcon("icon/appbar_save.png"))
        self.btn_save.setStyleSheet(Theme().RoundButton)
        self.btn_save.setIconSize(Qt.QSize(48, 48))

        layout_top = QtGui.QHBoxLayout()
        layout_top.addWidget(label_title)
        layout_top.addStretch()
        layout_top.addWidget(self.btn_back)
        layout_top.addWidget(self.btn_next)
        layout_top.addWidget(self.btn_today)
        layout_top.addWidget(self.btn_save)
        self.setFixedHeight(100)
        self.setStyleSheet(Theme().Theme)
        self.setLayout(layout_top)

        ls_1 = os.listdir("C:/")
        if "BingWallpage" not in ls_1:
            os.mkdir("C:/BingWallpage")

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = BarTop()
    mainWin.show()
    sys.exit(app.exec_())
