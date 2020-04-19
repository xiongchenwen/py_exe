import re
import sys
import sip
import matplotlib
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from TSP_Ui import Ui_MainWindow
import cal
import algorithm


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

    # —— —— —— 实际地块(可处理倾斜矩形) —— —— ——
    # Kml解析函数，返回GPS坐标值
    def Import_Kml(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './', "Kml Files(*.kml);;\All Files(*)")
        self.filename = fname[0]
        if fname[0]:
            f = open(fname[0], 'r', encoding='utf-8')
            with f:
                data = f.read()
            f.close()
            c = re.sub(r"\s|<|>", "", data)
            d = re.findall(r"([0-9]+\.[0-9]{13})", c)
            f = list(map(float, d[0::]))
            return f
        else:
            pass

    # GPS转UTM，并绘制实际地块。
    def UTM_field(self):
        self.F = MyFigure(width=3, height=2, dpi=100)
        d = self.Import_Kml()
        if d:
            x = []
            y = []
            for a in range(0, len(d) - 1, 2):
                m, n = cal.wgs84toutm(d[a], d[a + 1])
                x.append(m)
                y.append(n)
            x_move = x[0] - 20
            y_move = y[0] - 20
            for b in range(0, len(x)):
                x[b] = x[b] - x_move
                y[b] = y[b] - y_move
            self.F.axes.plot(x, y)
            self.F.axes.axis('equal')
            self.horizontalLayout.addWidget(self.F)
        else:
            pass

    # 设置步数，更新画布，调用UTM_field函数绘图
    def IMP_field(self):
        self.step += 1
        if self.step == 1:
            self.UTM_field()
        else:
            sip.delete(self.F)
            self.UTM_field()

    # 按钮0（pushButton）,调用实际地块显示更新
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.IMP_field()

    def Path_Info(self):
        path_width = float(self.lineEdit.text())
        offset_width = float(self.lineEdit_5.text())
        return path_width, offset_width

    #  实际地块路径显示
    def GPS_get(self):
        self.F = MyFigure(width=3, height=2, dpi=100)
        filename = self.filename
        if filename:
            f = open(filename, 'r', encoding="utf-8")
            with f:
                data = f.read()
            f.close()
            c = re.sub(r"\s|<|>", "", data)
            d = re.findall(r"([0-9]+\.[0-9]{13})", c)
            f = list(map(float, d[0::]))
            return f
        else:
            pass

    def UTM_get(self):
        d = self.GPS_get()
        if d:
            x = []
            y = []
            for a in range(0, len(d) - 1, 2):
                m, n = cal.wgs84toutm(d[a], d[a + 1])
                x.append(m)
                y.append(n)
            x_move = x[0] - 20
            y_move = y[0] - 20
            for b in range(0, len(x)):
                x[b] = x[b] - x_move
                y[b] = y[b] - y_move
            # self.F.axes.plot(x, y)
            del (x[-1])
            del (y[-1])
            return x, y
        else:
            pass

    def Drawing(self):
        point_1 = []
        x, y = self.UTM_get()
        for i in range(0, len(x)):
            point = []
            point.append(x[i])
            point.append(y[i])
            point_1.append(point)

        path_width, offset_width = self.Path_Info()
        path_width = path_width * 10
        # 扫描线间隔距离(车辆工作幅宽)
        # path_width = 4 * 10  # 全部数据扩大10倍，画图时在缩小即可，扫描线间隔是4（原因是程序中i不能产生浮点数）
        # 偏置距离（根据转弯来计算）
        d = int(path_width / 10)
        d_ = int(d * (offset_width + 1))
        point_ = []

        # 调用偏置程序 （import Polygon_offset as Pol）
        for x in range(0, d_, d):
            a = cal.Shrink(x, *point_1)
            point_.append(a)
        point_offset = point_[int((d_ / d) - 1)]

        # 多边形顶点数
        POINTNUM_1 = len(point_offset)
        point_1.append(point_1[0])
        P_x_ = []
        P_y_ = []
        for p in point_1:
            P_x_.append(p[0])
            P_y_.append(p[1])
        self.F.axes.plot(P_x_, P_y_)

        for i in range(1, int((d_ / d) - 1)):
            point_[i].append(point_[i][0])
            P_x_ = []
            P_y_ = []
            for p in point_[i]:
                P_x_.append(p[0])
                P_y_.append(p[1])
            self.F.axes.plot(P_x_, P_y_, color='red', linewidth=1)

        Polygon_1 = point_offset
        X = []
        Y = []
        for i in range(POINTNUM_1):
            x = (Polygon_1[i][0])
            y = (Polygon_1[i][1])
            X.append(x)
            Y.append(y)
        X.append(Polygon_1[0][0])
        Y.append(Polygon_1[0][1])
        algorithm.polyScan_Draw(self, point_1, point_offset, path_width)
        # 这一部分放在algorithm.py中，放这里会运行2次，加大计算量.
        # 结果展示内容
        # min_angle, min_distance = algorithm.polyScan(point_1, point_offset, path_width)
        # self.textBrowser.setText("最优角度: " + str(min_angle) + "\n最短距离: " + str(min_distance))
        self.F.axes.plot(X, Y, color='red', linewidth=1)
        self.F.axes.axis('equal')
        self.horizontalLayout.addWidget(self.F)

    def Call_update(self):
        self.step += 1
        if self.step == 1:
            self.Drawing()
        else:
            sip.delete(self.F)
            self.Drawing()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.Call_update()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    aw = Application()
    aw.show()
    sys.exit(qApp.exec_())