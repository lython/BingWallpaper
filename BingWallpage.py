#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib
import shutil
from PyQt4 import QtGui, QtCore, Qt, QtNetwork
from bar_top import BarTop
from bar_bottom import BarBottom


class BingWallPage(QtGui.QMainWindow):
    def __init__(self):
        super(BingWallPage, self).__init__()
        self.resize(1024, 768)
        self.setWindowIcon(QtGui.QIcon("icon/icon.png"))
        self.setWindowTitle(u"必应壁纸v1.0")

        QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)
        self.index = 0
        self.url = "http://bingimage.sinaapp.com/%s" % self.index

        self.view = QtGui.QLabel(self)
        self.view.setAlignment(QtCore.Qt.AlignCenter)
        self.view.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        self.view.setBackgroundRole(QtGui.QPalette.Dark)
        self.view.setAutoFillBackground(True)
        self.view.setPixmap(QtGui.QPixmap("./bing.jpg"))

        self.bar_top = BarTop()
        self.bar_bottom = BarBottom()

        self.bar_top.btn_back.clicked.connect(self.btn_back_click)
        self.bar_top.btn_next.clicked.connect(self.btn_next_click)
        self.bar_top.btn_today.clicked.connect(self.btn_today_click)
        self.bar_top.btn_save.clicked.connect(self.btn_save_click)

        splitter = QtGui.QSplitter(Qt.Qt.Vertical)
        splitter.addWidget(self.bar_top)
        splitter.addWidget(self.view)
        splitter.addWidget(self.bar_bottom)
        self.setCentralWidget(splitter)

    def btn_back_click(self):
        #前一天的图片
        if self.index < 16:
            self.index += 1
            url = "http://bingimage.sinaapp.com/%s" % self.index
            urllib.urlretrieve(url, "./bing.jpg")
        else:
            dlg = QtGui.QMessageBox(self)
            dlg.about(self, u"已经最多", u"对不起，微软服务器上最多只保存了最近17天的壁纸！")
        self.view.setPixmap(QtGui.QPixmap("./bing.jpg"))


    def btn_next_click(self):
        #返回上一张
        if self.index:
            self.index -= 1
            url = "http://bingimage.sinaapp.com/%s" % self.index
            urllib.urlretrieve(url, "./bing.jpg")
            self.view.setPixmap(QtGui.QPixmap("./bing.jpg"))
        else:
            dlg = QtGui.QMessageBox(self)
            dlg.about(self, u"空值", u"不能查看明天的必应壁纸！")

    def btn_today_click(self):
        #今天的图片
        self.index = 0
        url = "http://bingimage.sinaapp.com/0"
        urllib.urlretrieve(url, "./bing.jpg")
        self.view.setPixmap(QtGui.QPixmap("./bing.jpg"))

    def btn_save_click(self):
        #保存
        filename = unicode(QtGui.QFileDialog.getSaveFileName(self,
            u"保存必应壁纸...",
            u'Bing_%s' % self.index,
            u'图像(*.jpg)'))
        if filename:
            shutil.copy("./bing.jpg", filename)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = BingWallPage()
    mainWin.show()
    sys.exit(app.exec_())
