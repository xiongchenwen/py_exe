# 使用说明
# 程序运行后，通过鼠标选点进行画图（左键选点，右键取消）
# POINTNUM表示选择的顶点数目
# 扫描填充算法详解：https://blog.csdn.net/wodownload2/article/details/52154207?utm_source=distribute.pc_relevant.none-task


import matplotlib.pyplot as plt
import math

# import Polygon_offset as Pol

# 多边形顶点数
POINTNUM_1 = 6
POINTNUM_2 = 3
POINTNUM = POINTNUM_1 + POINTNUM_2
# 分辨率
LENGTH = 60

fig = plt.figure("扫描线填充算法", figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.axis([0, LENGTH, 0, LENGTH])

point_1 = [[50, 50], [20, 55], [10, 35], [20, 10], [40, 10], [55, 25]]
point_2 = [[30, 30], [40, 30], [30, 40]]

path_width = 3 * 10
angle = 45  # 旋转角度
radian = math.radians(angle)  # 角度转弧度
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
points_1 = [None] * POINTNUM_2


def paint():
    Polygon_1 = point_1
    X = []
    Y = []
    for i in range(POINTNUM_1):
        x = (Polygon_1[i][0])
        y = (Polygon_1[i][1])
        X.append(x)
        Y.append(y)

        x_1 = int(((x - b) * math.cos(-radian) - (y - b) * math.sin(-radian) + b) * 10)
        y_1 = int(((y - b) * math.cos(-radian) + (x - b) * math.sin(-radian) + b) * 10)
        print('y_1', y_1)
        points[i] = Point(x_1, y_1)

    X.append((Polygon_1[0][0]))
    Y.append((Polygon_1[0][1]))
    plt.plot(X, Y, color='blue', linewidth=1)

    Polygon_2 = point_2
    X_1 = []
    Y_1 = []
    for i in range(POINTNUM_2):
        x_1 = (Polygon_2[i][0])
        y_1 = (Polygon_2[i][1])
        X_1.append(x_1)
        Y_1.append(y_1)

        x_2 = int(((x_1 - b) * math.cos(-radian) - (y_1 - b) * math.sin(-radian) + b) * 10)
        y_2 = int(((y_1 - b) * math.cos(-radian) + (x_1 - b) * math.sin(-radian) + b) * 10)
        print('y_2', y_2)
        points_1[i] = Point(x_2, y_2)

    X_1.append((Polygon_2[0][0]))
    Y_1.append((Polygon_2[0][1]))
    plt.plot(X_1, Y_1, color='blue', linewidth=1)

    polyScan()
    plt.show()


def polyScan():
    MaxY = 0
    MinY = LENGTH * 10
    for i in range(POINTNUM_1):
        # print('points[i].y', points[i].y)
        if points[i].y > MaxY:
            MaxY = points[i].y
        if points[i].y < MinY:
            MinY = points[i].y
    print('MaxY', MaxY)
    print('MinY', MinY)
    a = MinY + path_width
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
                    print('j', j)

                if points[(j + 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
                    p = XET()
                    p.x = points[j].x
                    p.ymax = points[(j + 1 + POINTNUM_1) % POINTNUM_1].y
                    p.dx = (points[(j + 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
                            points[(j + 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
                    p.next = NET[i].next
                    NET[i].next = p
                    print('j', j)

        # 多边形内孔洞
        for k in range(POINTNUM_2):  # j为各顶点序号
            if points_1[k].y == i:
                # 一个点跟前面的一个点形成一条线段，跟后面的点也形成线段
                # 如果points[j].y较小就加入
                if points_1[(k - 1 + POINTNUM_2) % POINTNUM_2].y > points_1[k].y:
                    p = XET()
                    p.x = points_1[k].x
                    p.ymax = points_1[(k - 1 + POINTNUM_2) % POINTNUM_2].y
                    p.dx = (points_1[(k - 1 + POINTNUM_2) % POINTNUM_2].x - points_1[k].x) / (
                            points_1[(k - 1 + POINTNUM_2) % POINTNUM_2].y - points_1[k].y)
                    p.next = NET[i].next
                    NET[i].next = p
                    print('k', k)

                if points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].y > points_1[k].y:
                    p = XET()
                    p.x = points_1[k].x
                    p.ymax = points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].y
                    p.dx = (points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].x - points_1[k].x) / (
                            points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].y - points_1[k].y)
                    p.next = NET[i].next
                    NET[i].next = p
                    print('k', k)

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

        # 配对填充颜色
        if i == a:
            p = AET.next
            while p and p.next:
                j_1 = p.x / 10
                # print('j_1',j_1)
                # y = i
                j_2 = p.next.x / 10
                # X = [j_1, j_2]
                # Y = [i, i]
                x_1 = ((j_1 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_1 = ((j_1 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                x_2 = ((j_2 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_2 = ((j_2 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                X = [x_1, x_2]
                Y = [y_1, y_2]
                plt.plot(X, Y, color='red', linewidth=0.5)
                # print('X', X)
                # print('Y', Y)

                # 考虑端点情况
                p = p.next.next
                # print('a', a)
            a += path_width


if __name__ == "__main__":
    paint()
