# 多边形偏置的支持程序，目前是能偏置一次，地面机械应该多次偏置（后续改进）。
# 初始多边形偏置程序的改进版
# 本算法参考文献：熊文骏. 向形心收缩的变距偏置填充算法[D].华中科技大学,2007.
# numpy求解二元一次方程：https://zhidao.baidu.com/question/1706135878772500620.html
# 此程序中点必须“逆时针”方向输入

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def Shrink(d, *p):
    # 下面部分功能多边形旋转（此程序中公式以点逆时针为求解条件）
    # 将点顺时针转为逆时针
    p_list = len(p)
    p_max = p.index(max(p))
    x_1 = p[p_max - 1][0]
    y_1 = p[p_max - 1][1]
    x_2 = p[p_max][0]
    y_2 = p[p_max][1]
    if p_max + 1 == p_list:
        x_3 = p[0][0]
        y_3 = p[0][1]
    else:
        x_3 = p[p_max + 1][0]
        y_3 = p[p_max + 1][1]
    p12_p23 = (x_2 - x_1) * (y_3 - y_2) - (y_2 - y_1) * (x_3 - x_2)
    if p12_p23 >= 0:
        p = p
    else:
        p = list(reversed(p))
    p = list(p)  # 元组转换成列表
    p.append(p[0])  # 再次添加第一个点，起封闭图形作用。
    print(p)
    # 多边形旋转结束，输出坐标

    point_1 = []
    P_x = []
    P_y = []
    Px = []
    Py = []
    len_mark = len(p)
    line = []
    line_1 = []
    line_ = []
    L_ = []

    # 求解偏移直线的a、b、c。 ax+by=c，由所述的截距式转换而来。
    for m in range(len_mark - 1):
        dx = p[m + 1][0] - p[m][0]
        dy = p[m + 1][1] - p[m][1]
        c1 = p[m + 1][0] * p[m][1] - p[m][0] * p[m + 1][1]
        L = ((p[m + 1][0] - p[m][0]) ** 2 + (p[m + 1][1] - p[m][1]) ** 2) ** .5  # 各边的长度
        # print('L', L)
        c2 = L * d
        if dx > 0 or dx < 0:
            a = -dy / dx
            b = 1
            c = (c1 + c2) / dx
        if dx == 0:
            if dy > 0:
                a = 1
                b = 0
                c = p[m][0] - d
            if dy < 0:
                a = 1
                b = 0
                c = p[m][0] + d
        L_.append(L)
        line.append([a, b, c])
        line_.append([a, b, c])
    line_.append(line[0])  # 再将第一条直线加入
    print('line_', line_)

    # 解决多边形偏置过程中环自交问题，
    # 求每一条边与左右边的交点，通过判断x坐标点（或者y坐标点）的大小，判断是否自交
    # 其中有4个不同的情况（边与x轴平行时，边与y轴平行时）可参考上面论文理解
    # 将每一条边加入判断
    for i in range(0, len(line)):
        Px = []
        Py = []
        line_1 = []
        print('i', i)
        # 边与x轴平行时
        if p[i][0] > p[i + 1][0]:
            if i + 2 == len_mark:
                line_1.append(line[0])
            else:
                line_1.append(line[i + 1])
            line_1.append(line[i])
            line_1.append(line[i - 1])

        elif p[i][0] < p[i + 1][0]:
            line_1.append(line[i - 1])
            line_1.append(line[i])
            if i + 2 == len_mark:
                line_1.append(line[0])
            else:
                line_1.append(line[i + 1])

            # 求i线与左右线的交点，并判断x坐标大小，当偏移较大，则删除自交边
            for x in range(len(line_1) - 1):
                a = np.array([[line_1[x][0], line_1[x][1]], [line_1[x + 1][0], line_1[x + 1][1]]])
                b = np.array([line_1[x][2], line_1[x + 1][2]])
                c = np.linalg.solve(a, b)
                c = c.tolist()
                Px.append(c[0])
            if Px[0] > Px[1]:
                del line_[i]

        # 边与y轴平行时
        elif p[i][0] == p[i + 1][0]:
            if p[i][1] > p[i + 1][1]:
                if i + 2 == len_mark:
                    line_1.append(line[0])
                else:
                    line_1.append(line[i + 1])
                line_1.append(line[i])
                line_1.append(line[i - 1])
            else:
                line_1.append(line[i - 1])
                line_1.append(line[i])
                if i + 2 == len_mark:
                    line_1.append(line[0])
                else:
                    line_1.append(line[i + 1])

                for x in range(len(line_1) - 1):
                    a = np.array([[line_1[x][0], line_1[x][1]], [line_1[x + 1][0], line_1[x + 1][1]]])
                    b = np.array([line_1[x][2], line_1[x + 1][2]])
                    c = np.linalg.solve(a, b)
                    c = c.tolist()
                    Py.append(c[1])
                if Py[0] > Py[1]:
                    del line_[i]
    print('line_', line_)

    # 开始计算最终偏移直线的交点，坐标点point_1用于扫描线求解。
    for x in range(len(line_) - 1):
        a = np.array([[line_[x][0], line_[x][1]], [line_[x + 1][0], line_[x + 1][1]]])
        b = np.array([line_[x][2], line_[x + 1][2]])
        c = np.linalg.solve(a, b)
        c = c.tolist()
        point_1.append(c)
        P_x.append(c[0])
        P_y.append(c[1])
    return point_1


