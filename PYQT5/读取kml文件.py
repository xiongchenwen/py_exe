import re
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

from TSP_Ui import Ui_MainWindow
import cal


# —— —— —— 绘图画布初始 —— —— ——
# 绘图画布
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)


# # 绘图主函数
# class Application(QMainWindow, Ui_MainWindow):
#     step = 0
#     #	引入一个路径变量，这样可以将文件引入以及，结果用连个按钮分步进行。
#     filename = None
#
#     def __init__(self, parent=None):
#         super(Application, self).__init__(parent)
#         self.setupUi(self)
#     # —— —— —— 实际地块(可处理倾斜矩形) —— —— ——
#     # Kml解析函数，返回GPS坐标值
#     def Import_Kml(self):
#         fname = QFileDialog.getOpenFileName(self, '打开文件', './', "Kml Files(*.kml);;\
# 			All Files(*)")
#         self.filename = fname[0]
#         if fname[0]:
#             #			f = QtCore.QFile(fname[0])
#             f = open(fname[0], 'r', encoding='utf-8')
#             with f:
#                 data = f.read()
#             f.close()
#             c = re.sub(r"\s|<|>", "", data)
#             d = re.findall(r"([0-9]+\.[0-9]{13})", c)
#             f = list(map(float, d[0::]))
#             print('f', f)
#             return f
#         else:
#             pass
#
#     # GPS转UTM，并绘制实际地块。
#     def UTM_field(self):
#         self.F = MyFigure(width=3, height=2, dpi=100)
#         d = self.Import_Kml()
#         print('d', d)
#         if d:
#             x = []
#             y = []
#             for a in range(0, len(d) - 1, 2):
#                 m, n = cal.wgs84toutm(d[a], d[a + 1])
#                 print('m', m)
#                 print('n', n)
#                 x.append(m)
#                 y.append(n)
#             print('x', x)
#             print('y', y)
#             x_move = x[0] - 20
#             y_move = y[0] - 20
#             for b in range(0, len(x)):
#                 x[b] = x[b] - x_move
#                 y[b] = y[b] - y_move
#             print('x', x)
#             print('y', y)
#             self.F.axes.plot(x, y)
#             self.F.axes.axis('equal')
#             self.horizontalLayout.addWidget(self.F)
#         else:
#             pass
#
#     # 设置步数，更新画布，调用UTM_field函数绘图
#     def IMP_field(self):
#         self.step += 1
#         if self.step == 1:
#             self.UTM_field()
#         else:
#             sip.delete(self.F)
#             self.UTM_field()
#
#     # 按钮3,调用实际地块显示更新
#     @pyqtSlot()
#     def on_pushButton_3_clicked(self):
#         self.IMP_field()

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()
File_path = filedialog.askopenfilename()  # 获得选择好的文件
text = ' '
file = open(File_path)
for line in file:
    text = text + line
file.close()
c = re.sub(r"\f|\n|\r|\t|<|>", "", text)
d = re.findall(r"coordinates(.+?)/coordinates", c)

for i in d:
    e = (re.sub(r"0 ", "", i))
    f = re.findall(r"([0-9]+\.[0-9]{13})", e)
    d = list(map(float, f[0::]))
    if d:
        x = []
        y = []
        for a in range(0, len(d) - 1, 2):
            m, n = cal.wgs84toutm(d[a], d[a + 1])
            x.append(m)
            y.append(n)
        x_move = x[0]
        y_move = y[0]
        for b in range(0, len(x)):
            x[b] = x[b] - x_move + 20
            y[b] = y[b] - y_move + 20

    plt.plot(x, y, color='blue', linewidth=1)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    aw = Application()
    aw.show()
    sys.exit(qApp.exec_())
