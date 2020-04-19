import os
import sys
import math
import random
import matplotlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget, \
    QFileDialog
import matplotlib

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from manage import *
from numpy import arange, sin, pi
from newuiv4_4 import Ui_MainWindow
import sip
import calculate as cal
import re
import datetime

path_width = 50


# —— —— —— 绘图画布初始 —— —— ——
# 绘图画布
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)


# 绘图主函数
class Application(QMainWindow, Ui_MainWindow):
    step = 0
    # 引入一个路径变量，这样可以将文件引入以及，结果用连个按钮分步进行。
    filename = None

    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)

    def Import_Kml(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './', "Kml Files(*.kml);;\
			All Files(*)")
        self.filename = fname[0]
        if fname[0]:
            f = open(fname[0], 'r', encoding='utf-8')
            with f:
                data = f.read()
                f.close()
                c = re.sub(r"\f|\n|\r|\t|<|>", "", data)
                d = re.findall(r"coordinates(.+?)/coordinates", c)
                for i in d:
                    e = (re.sub(r"0 ", "", i))
                    f = re.findall(r"([0-9][0-9]+\.+[0-9]{10})", e)
                    g = list(map(float, (f[0::2])))
        return d, g

    def UTM_field(self):
        self.F = MyFigure(width=3, height=2, dpi=100)
        d, g = self.Import_Kml()
        POINTNUM = len(g)
        for i in d:
            e = (re.sub(r"0 ", "", i))
            f = re.findall(r"([0-9][0-9]+\.+[0-9]{10})", e)
            g = list(map(float, (f[0::2])))
            h = list(map(float, (f[1::2])))
            X = []
            Y = []
            for a in range(0, POINTNUM):
                m, n = cal.wgs84toutm(g[a], h[a])
                X.append(m)
                Y.append(n)
            self.F.axes.plot(X, Y, linewidth=1, color="blue")
            self.F.axes.axis('equal')
            self.horizontalLayout.addWidget(self.F)

    def IMP_field(self):
        self.step += 1
        if self.step == 1:
            self.UTM_field()
        else:
            sip.delete(self.F)
            self.UTM_field()

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.IMP_field()

    #  实际地块路径显示
    def Path_Info(self):
        path_width = float(self.lineEdit_5.text())
        offset_width = float(self.lineEdit.text())
        return path_width, offset_width

    def GPS_get(self):
        self.F = MyFigure(width=3, height=2, dpi=100)
        filename = self.filename
        if filename:
            f = open(filename, 'r', encoding="utf-8")
            with f:
                data = f.read()
            f.close()
            c = re.sub(r"\f|\n|\r|\t|<|>", "", data)
            d = re.findall(r"coordinates(.+?)/coordinates", c)
            for i in d:
                e = (re.sub(r"0 ", "", i))
                f = re.findall(r"([0-9][0-9]+\.+[0-9]{10})", e)
                g = list(map(float, (f[0::2])))
            return d, g

    def UTM_get(self):
        d, g = self.GPS_get()
        POINTNUM = len(g)
        for i in d:
            e = (re.sub(r"0 ", "", i))
            f = re.findall(r"([0-9][0-9]+\.+[0-9]{10})", e)
            g = list(map(float, (f[0::2])))
            h = list(map(float, (f[1::2])))
            x = []
            y = []
            for a in range(0, POINTNUM):
                m, n = cal.wgs84toutm(g[a], h[a])
                x.append(int(m))
                y.append(int(n))
            print(x)
            self.F.axes.plot(x, y, color="blue")
            print('x',x)
            return x, y

    def Scan_Line(self):
        x, y = self.UTM_get()
        path_width, offset_width = self.Path_Info()
        xy = [list(i) for i in list(zip(x, y))]
        print('xy',xy)
        shink = cal.Shrink(-offset_width, *xy)
        a = shink[0]
        b = shink[1]
        POINTNUM = len(a)
        points = [None] * POINTNUM
        ab = list(zip(a, b))
        X = []
        Y = []
        for i in range(len(shink[0])):
            x = int(ab[i][0])
            y = int(ab[i][1])
            X.append(x)
            Y.append(y)
            points[i] = Point(x, y)
        polyScan(self, POINTNUM, points, path_width)
        print('X', X)
        print('Y', Y)
        return X, Y

    def IMP_Field_display(self):
        x, y = self.Scan_Line()
        self.F.axes.plot(x, y, linewidth=1, color="red")
        self.F.axes.axis('equal')
        self.horizontalLayout.addWidget(self.F)

    def Call_update(self):
        self.step += 1
        if self.step == 1:
            self.IMP_Field_display()
        else:
            sip.delete(self.F)
            self.IMP_Field_display()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.Call_update()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    aw = Application()
    aw.show()
    sys.exit(qApp.exec_())
