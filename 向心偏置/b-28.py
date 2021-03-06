# 本算法参考文献：熊文骏. 向形心收缩的变距偏置填充算法[D].华中科技大学,2007.
# numpy求解二元一次方程：https://zhidao.baidu.com/question/1706135878772500620.html
# 此程序中点必须“逆时针”方向输入

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

d = 2
d_ = 4
# p = [[16, 6], [20, 14], [19, 21], [8, 19], [8, 12], [12, 6], [16, 6]]
p = [[16, 6], [12, 6], [8, 12], [8, 19], [19, 21], [20, 15]]
P_x_ = []
P_y_ = []

# 此程序中点必须“逆时针”方向输入
# 如何判断多边形是顺时针绘制还是逆时针绘制
# 并将其转为逆时针（参考：https://blog.csdn.net/D_bel/article/details/94005841）
p_list = len(p)
p_max = p.index(max(p))
x_1 = p[p_max-1][0]
y_1 = p[p_max-1][1]
x_2 = p[p_max][0]
y_2 = p[p_max][1]
if p_max+1 == p_list:
    x_3 = p[0][0]
    y_3 = p[0][1]
else:
    x_3 = p[p_max + 1][0]
    y_3 = p[p_max + 1][1]
p12_p23 = (x_2-x_1)*(y_3-y_2)-(y_2-y_1)*(x_3-x_2)
if p12_p23 >= 0:
    p = p
else:
    p = list(reversed(p))
p.append(p[0])   # 再次添加第一个点，起封闭图形作用。


def Shrink(d, *p):
    P_x = []
    P_y = []
    Px = []
    len_mark = len(p)
    line = []
    line_1 = []
    L_ = []

    # 求解偏移直线的a、b、c。 ax+by=c，由所述的截距式转换而来。
    for m in range(len_mark - 1):
        dx = p[m + 1][0] - p[m][0]
        dy = p[m + 1][1] - p[m][1]
        c1 = p[m + 1][0] * p[m][1] - p[m][0] * p[m + 1][1]
        L = ((p[m + 1][0] - p[m][0]) ** 2 + (p[m + 1][1] - p[m][1]) ** 2) ** .5    # 各边的长度
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

    # 找到最短的线，以及左右2条线
    L_min = L_.index(min(L_))
    line_1.append(line[L_min - 1])
    line_1.append(line[L_min])
    line_1.append(line[L_min + 1])
    line.append(line[0])  # 再将第一条直线加入


    # 求最短线与左右线的交点，并判断x坐标大小，当出现偏移较大，则删除最短边。
    for x in range(len(line_1)-1):
        a = np.array([[line_1[x][0], line_1[x][1]], [line_1[x + 1][0], line_1[x + 1][1]]])
        b = np.array([line_1[x][2], line_1[x + 1][2]])
        c = np.linalg.solve(a, b)
        c = c.tolist()
        Px.append(c[0])
    if Px[0] > Px[1]:
        del line[L_min]

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
    a = Shrink(d, *p)
    plt.plot(*a, color="red")

for p in p:
    P_x_.append(p[0])
    P_y_.append(p[1])

plt.plot(P_x_, P_y_, color="blue")
plt.axis("equal")
plt.show()
