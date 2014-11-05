#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'LIJ'

class Theme():
    def __init__(self):
        self.ThemeRGB = "#333333"
        self.Theme = "background-color:%s" % self.ThemeRGB
        self.ThemeButton = """QPushButton{background-color:white;border:2px groove %s;}
                 QPushButton:hover{background-color:%s;}
                 QPushButton:pressed{background-color:gray;}
                 QPushButton:checked{background-color:#0050EF;}
                 QPushButton{font-family:"微软雅黑";font-size:15px;}
                 QPushButton:disabled{color:gray;border:2px groove gray;}""" % (self.ThemeRGB, self.ThemeRGB)

        self.WhiteButton = u"""QPushButton{color:white;background-color:transparent;border:2px groove white;}
                  QPushButton:hover{background-color:#1BAEE2;}
                  QPushButton:pressed{background-color:gray;}
                  QPushButton{width:100;height:30;}
                  QPushButton{font-family:"微软雅黑";font-size:15px;}
                  QPushButton:checked{background-color:#0000ff;}
                  QPushButton:disabled{color:#636562;border:2px groove #636562;}"""

        self.ToggleButton = """QPushButton{background-color:transparent;border-radius:5px;}
                                           QPushButton:hover{background-color:#1BAEE2;}
                                           QPushButton:pressed{background-color:gray;}"""

        self.RoundButton = """QToolButton{background-color:transparent;border-radius:24px;}
                 QToolButton{width:48;height:48;}
                 QToolButton:hover{background-color:#1BAEE2;}
                 QToolButton:disabled{background-color:gray;border-radius:24px;}"""

        self.IconTextButton = """QToolButton{color:white;background-color:transparent;border-radius:0px;}
                 QToolButton:hover{background-color:#1BAEE2;}
                 QToolButton{width:80;height:80;}
                 QToolButton:pressed{background-color:gray;}"""

        self.RedButton = u"""QPushButton{color:white;background-color:#A20025;border:2px groove white;}"""

        self.GreenButton = u"""QPushButton{color:white;background-color:#60A917;border:2px groove white;}"""

        self.BreakButton = u"""QPushButton{color:white;background-color:#60A917;border:2px groove white;}
                  QPushButton:checked{background-color:#A20025;}
                  QPushButton:disabled{color:#636562;border:2px groove #636562;}"""

        self.ToastLabel = u"""QLabel{color:white;background-color:#00ABA9;font-size:22px;font-family:"微软雅黑";
                          border:0px groove white;}"""

        self.ErrorLabel = u"""QLabel{color:white;background-color:transparent;font-size:24px;font-family:"微软雅黑";
                          border:0px groove white;}"""

        self.ErrorLabelsub = u"""QLabel{color:white;background-color:transparent;font-size:20px;font-family:"微软雅黑";
                          border:0px groove white;}"""

        self.BatteryProgressOut = """QProgressBar { border: 0px solid gray; color:red;background: transparent;}"""

        self.ToolTip = """QToolTip{border: 2px solid DodgerBlue;padding: 2px;
        color: white; background: #040b1e;border-radius: 2px;}"""


