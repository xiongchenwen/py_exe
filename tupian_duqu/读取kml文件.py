import re
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

import cal

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()
File_path = filedialog.askopenfilename()   # 获得选择好的文件
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
    # print('d', d)
    if d:
        x = []
        y = []
        for a in range(0, len(d) - 1, 2):
            m, n = cal.wgs84toutm(d[a], d[a + 1])
            # print('m', m)
            # print('n', n)
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




