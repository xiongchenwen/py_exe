import re
import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

import cal

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
    # print('d', d)
    if d:
        point = []
        x = []
        y = []
        for a in range(0, len(d) - 3, 2):
            m, n = cal.wgs84toutm(d[a], d[a + 1])
            # print('m', m)
            # print('n', n)
            x.append(m)
            y.append(n)
        x_move = x[0]
        y_move = y[0]
        for i in range(0, len(x)):
            x[i] = x[i] - x_move + 20
            y[i] = y[i] - y_move + 20
            point.append([x[i], y[i]])

# import Polygon_offset as Pol

# 分辨率
# LENGTH = 60

fig = plt.figure("扫描线填充算法", figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
# ax.axis([0, LENGTH, 0, LENGTH])

point_1 = point

# 多边形顶点数
POINTNUM_1 = len(point_1)
POINTNUM = POINTNUM_1

# 扫描线间隔距离
path_width = 6 * 10
# 多边形顺时针旋转
b = max(point_1[1])  # 绕(b,b)旋转,b为y轴最大值


# 定义边的结构
class XET:
    def __init__(self, x=0.0, dx=0.0, ymax=0):
        self.x = x
        self.dx = dx
        self.ymax = ymax
        self.next = None


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [None] * POINTNUM_1


def paint():
    Polygon_1 = point_1
    X = []
    Y = []
    for i in range(POINTNUM_1):
        x = (Polygon_1[i][0])
        y = (Polygon_1[i][1])
        X.append(x)
        Y.append(y)
    X.append((Polygon_1[0][0]))
    Y.append((Polygon_1[0][1]))
    plt.plot(X, Y, color='blue', linewidth=1)

    polyScan()
    plt.axis('equal')
    plt.show()


def polyScan():
    angle = 0  # 初始旋转角度
    distance_set = []
    for i in range(0, 180):
        if angle <= 180:
            radian = math.radians(angle)  # 角度转弧度

            Polygon_1 = point_1
            for i in range(POINTNUM_1):
                x = (Polygon_1[i][0])
                y = (Polygon_1[i][1])
                x_1 = int(((x - b) * math.cos(-radian) - (y - b) * math.sin(-radian) + b) * 10)
                y_1 = int(((y - b) * math.cos(-radian) + (x - b) * math.sin(-radian) + b) * 10)
                points[i] = Point(x_1, y_1)

            MaxY = 0
            MinY = 1000 * 10
            for i in range(POINTNUM_1):
                if points[i].y > MaxY:
                    MaxY = points[i].y
                if points[i].y < MinY:
                    MinY = points[i].y
            # print('MaxY', MaxY)
            # print('MinY', MinY)

            c = MinY + path_width / 2
            # 总距离
            t_distance = 0
            # 初始化AET表
            AET = XET()
            # 初始化NET表
            NET = [None] * (MaxY + 1)
            for i in range(MaxY + 1):
                NET[i] = XET()

            # 扫描并建立NET表
            for i in range(MaxY + 1):  # i为y坐标
                for j in range(POINTNUM_1):  # j为各顶点序号
                    if points[j].y == i:
                        # 一个点跟前面的一个点形成一条线段，跟后面的点也形成线段
                        # 如果points[j].y较小就加入
                        if points[(j - 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
                            p = XET()
                            p.x = points[j].x
                            p.ymax = points[(j - 1 + POINTNUM_1) % POINTNUM_1].y
                            p.dx = (points[(j - 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
                                    points[(j - 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
                            p.next = NET[i].next
                            NET[i].next = p

                        if points[(j + 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
                            p = XET()
                            p.x = points[j].x
                            p.ymax = points[(j + 1 + POINTNUM_1) % POINTNUM_1].y
                            p.dx = (points[(j + 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
                                    points[(j + 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
                            p.next = NET[i].next
                            NET[i].next = p

            # print('NET', NET)

            # 建立并更新活性边表AET
            for i in range(MinY, MaxY + 1):
                # 计算新的交点x（p.x）, 更新AET
                p = AET.next
                while p:
                    p.x = p.x + p.dx
                    p = p.next
                # print('i', i)
                # 更新后新AET先排序
                # 断表排序, 不再开辟空间
                tq = AET
                p = AET.next
                tq.next = None  # tq中最后一个取值为None
                while p:
                    while tq.next and p.x >= tq.next.x:
                        tq = tq.next
                    s = p.next
                    p.next = tq.next
                    tq.next = p
                    p = s
                    tq = AET
                # (改进算法)
                # 先从AET表中删除ymax == i的结点
                q = AET
                p = q.next
                while p:
                    if p.ymax == i:
                        q.next = p.next  # 删除了ymax == i时的x dx ymax
                        p = q.next
                    else:
                        q = q.next
                        p = q.next

                # 将NET中的新点加入AET, 并用插入法按X值递增排序
                p = NET[i].next
                q = AET
                while p:
                    while q.next and p.x >= q.next.x:
                        q = q.next
                    s = p.next
                    p.next = q.next
                    q.next = p
                    p = s
                    q = AET

                if i == c:
                    p = AET.next
                    while p and p.next:
                        j_1 = p.x / 10
                        j_2 = p.next.x / 10
                        x_1 = ((j_1 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                        y_1 = ((j_1 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                        x_2 = ((j_2 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                        y_2 = ((j_2 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                        distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
                        t_distance += distance
                        # 考虑端点情况
                        p = p.next.next
                    c += path_width
            distance_set.append(t_distance)
            angle += 1
            # print('总距离', round(t_distance, 3))  # round 保留3位小数
        else:
            pass
    #     print('angle', angle-1)
    # print('distance_set', distance_set)
    min_angle = distance_set.index(min(distance_set))
    min_distance = min(distance_set)
    print('最短距离_角度', min_angle)
    print('最短距离', min_distance)

    #################################################################################
    # 此次算法重复上面，最后加上画图。（可以精简，暂时未解决）
    radian = math.radians(min_angle)  # 角度转弧度
    Polygon_1 = point_1
    for i in range(POINTNUM_1):
        x = (Polygon_1[i][0])
        y = (Polygon_1[i][1])
        x_1 = int(((x - b) * math.cos(-radian) - (y - b) * math.sin(-radian) + b) * 10)
        y_1 = int(((y - b) * math.cos(-radian) + (x - b) * math.sin(-radian) + b) * 10)
        points[i] = Point(x_1, y_1)

    MaxY = 0
    MinY = 1000 * 10
    for i in range(POINTNUM_1):
        if points[i].y > MaxY:
            MaxY = points[i].y
        if points[i].y < MinY:
            MinY = points[i].y
    # print('MaxY', MaxY)
    # print('MinY', MinY)

    a = MinY + path_width
    c = MinY + path_width / 2
    # 总距离
    t_distance = 0
    # 初始化AET表
    AET = XET()
    # 初始化NET表
    NET = [None] * (MaxY + 1)
    for i in range(MaxY + 1):
        NET[i] = XET()

    # 扫描并建立NET表
    for i in range(MaxY + 1):  # i为y坐标
        for j in range(POINTNUM_1):  # j为各顶点序号
            if points[j].y == i:
                # 一个点跟前面的一个点形成一条线段，跟后面的点也形成线段
                # 如果points[j].y较小就加入
                if points[(j - 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
                    p = XET()
                    p.x = points[j].x
                    p.ymax = points[(j - 1 + POINTNUM_1) % POINTNUM_1].y
                    p.dx = (points[(j - 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
                            points[(j - 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
                    p.next = NET[i].next
                    NET[i].next = p

                if points[(j + 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
                    p = XET()
                    p.x = points[j].x
                    p.ymax = points[(j + 1 + POINTNUM_1) % POINTNUM_1].y
                    p.dx = (points[(j + 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
                            points[(j + 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
                    p.next = NET[i].next
                    NET[i].next = p

    # print('NET', NET)

    # 建立并更新活性边表AET
    for i in range(MinY, MaxY + 1):
        # 计算新的交点x（p.x）, 更新AET
        p = AET.next
        while p:
            p.x = p.x + p.dx
            p = p.next
        # print('i', i)
        # 更新后新AET先排序
        # 断表排序, 不再开辟空间
        tq = AET
        p = AET.next
        tq.next = None  # tq中最后一个取值为None
        while p:
            while tq.next and p.x >= tq.next.x:
                tq = tq.next
            s = p.next
            p.next = tq.next
            tq.next = p
            p = s
            tq = AET
        # (改进算法)
        # 先从AET表中删除ymax == i的结点
        q = AET
        p = q.next
        while p:
            if p.ymax == i:
                q.next = p.next  # 删除了ymax == i时的x dx ymax
                p = q.next
            else:
                q = q.next
                p = q.next

        # 将NET中的新点加入AET, 并用插入法按X值递增排序
        p = NET[i].next
        q = AET
        while p:
            while q.next and p.x >= q.next.x:
                q = q.next
            s = p.next
            p.next = q.next
            q.next = p
            p = s
            q = AET

        # 从这里计算总距离，并比较大小，输出最大的角度
        # 然后画图

        # 配对填充颜色
        if i == a:
            p = AET.next
            while p and p.next:
                j_1 = p.x / 10
                j_2 = p.next.x / 10
                x_1 = ((j_1 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_1 = ((j_1 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                x_2 = ((j_2 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_2 = ((j_2 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                X = [x_1, x_2]
                Y = [y_1, y_2]
                plt.plot(X, Y, color='green', linewidth=0.5)

                # 考虑端点情况
                p = p.next.next
            a += path_width

        # 画车辆行驶路线
        if i == c:
            p = AET.next
            while p and p.next:
                j_1 = p.x / 10
                j_2 = p.next.x / 10
                x_1 = ((j_1 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_1 = ((j_1 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                x_2 = ((j_2 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_2 = ((j_2 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                X = [x_1, x_2]
                Y = [y_1, y_2]
                plt.plot(X, Y, color='red', linewidth=0.25, linestyle='--', dashes=[20, 15])  # dashes设置虚线间隔
                distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
                t_distance += distance
                # 考虑端点情况
                p = p.next.next
            c += path_width


if __name__ == "__main__":
    paint()
