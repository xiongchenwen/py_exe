# 本算法参考文献：熊文骏. 向形心收缩的变距偏置填充算法[D].华中科技大学,2007.
# numpy求解二元一次方程：https://zhidao.baidu.com/question/1706135878772500620.html

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

d = 2
d_ = 3
p = [[16, 6], [19, 13], [19, 21], [8, 19], [8, 12], [12, 6], [16, 6]]
P_x_ = []
P_y_ = []


def Shrink(d, *p):
    P_x = []
    P_y = []
    len_mark = len(p)
    line = []
    print("p", p)
    # 求解偏移直线的a、b、c。 ax+by=c，由所述的截距式转换而来。

    for m in range(len_mark - 1):
        dx = p[m + 1][0] - p[m][0]
        dy = p[m + 1][1] - p[m][1]
        c1 = p[m + 1][0] * p[m][1] - p[m][0] * p[m + 1][1]
        L = ((p[m + 1][0] - p[m][0]) ** 2 + (p[m + 1][1] - p[m][1]) ** 2) ** .5
        c2 = L * d
        if dx > 0:
            a = -dy / dx
            b = 1
            c = (c1 + c2) / dx
        if dx < 0:
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
        line.append([a, b, c])
    line.append(line[0])

    # 开始计算偏移直线的交点。

    for x in range(len(line) - 1):
        a = np.array([[line[x][0], line[x][1]], [line[x + 1][0], line[x + 1][1]]])
        b = np.array([line[x][2], line[x + 1][2]])
        c = np.linalg.solve(a, b)
        c = c.tolist()
        P_x.append(c[0])
        P_y.append(c[1])
    P_x.append(P_x[0])
    P_y.append(P_y[0])
    return [P_x, P_y]


for x in range(d_):
    print(x)
    a = Shrink(x, *p)
    plt.plot(*a, color="blue")

# for p in p:
#     P_x_.append(p[0])
#     P_y_.append(p[1])
#
# plt.plot(P_x_, P_y_, color="blue")
plt.axis("equal")
plt.show()
