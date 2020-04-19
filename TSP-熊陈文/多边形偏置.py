# 使用说明
# 程序运行后，通过鼠标选点进行画图（左键选点，右键取消）
# POINTNUM表示选择的顶点数目
# 扫描填充算法详解：https://blog.csdn.net/wodownload2/article/details/52154207?utm_source=distribute.pc_relevant.none-task


import matplotlib.pyplot as plt
import Polygon_offset as Pol

# 多边形顶点数
POINTNUM_1 = 6
POINTNUM_2 = 3
POINTNUM = POINTNUM_1 + POINTNUM_2
# 分辨率
LENGTH = 60

fig = plt.figure("扫描线填充算法", figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.axis([0, LENGTH, 0, LENGTH])

path_width = 3
d = 3

point_1 = [[50, 50], [20, 55], [10, 35], [20, 10], [40, 10], [55, 25]]
point_2 = [[30, 30], [40, 30], [30, 40]]
# # 如果没有孔洞。写一个判断，赋值如下：
# point_2 = [[0, 0], [0, 0], [0, 0]]

point_offset = Pol.Shrink(d, *point_1)
print('point_offset', point_offset)


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


# print('points', points)

def paint():
    point_1.append(point_1[0])
    P_x_ = []
    P_y_ = []
    for p in point_1:
        P_x_.append(p[0])
        P_y_.append(p[1])
    plt.plot(P_x_, P_y_, color="blue")

    Polygon_1 = point_offset
    X = []
    Y = []
    for i in range(POINTNUM_1):
        x = int(Polygon_1[i][0])
        y = int(Polygon_1[i][1])
        X.append(x)
        Y.append(y)
        points[i] = Point(x, y)
    X.append(int(Polygon_1[0][0]))
    Y.append(int(Polygon_1[0][1]))
    plt.plot(X, Y, color='red', linewidth=1)

    Polygon_2 = point_2
    X_1 = []
    Y_1 = []
    for i in range(POINTNUM_2):
        x_1 = int(Polygon_2[i][0])
        y_1 = int(Polygon_2[i][1])
        X_1.append(x_1)
        Y_1.append(y_1)
        points_1[i] = Point(x_1, y_1)
    X_1.append(int(Polygon_2[0][0]))
    Y_1.append(int(Polygon_2[0][1]))
    plt.plot(X_1, Y_1, color='red', linewidth=1)

    polyScan()
    plt.show()


def polyScan():
    MaxY = 0
    MinY = LENGTH
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

                if points[(j + 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
                    p = XET()
                    p.x = points[j].x
                    p.ymax = points[(j + 1 + POINTNUM_1) % POINTNUM_1].y
                    p.dx = (points[(j + 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
                            points[(j + 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
                    p.next = NET[i].next
                    NET[i].next = p

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

                if points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].y > points_1[k].y:
                    p = XET()
                    p.x = points_1[k].x
                    p.ymax = points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].y
                    p.dx = (points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].x - points_1[k].x) / (
                            points_1[(k + 1 + POINTNUM_2) % POINTNUM_2].y - points_1[k].y)
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
                j_1 = p.x
                # print('j_1',j_1)
                # y = i
                j_2 = p.next.x
                X = [j_1, j_2]
                Y = [i, i]
                plt.plot(X, Y, color='red', linewidth=0.5)

                # 考虑端点情况
                p = p.next.next
                # print('a', a)
            a += path_width


if __name__ == "__main__":
    paint()
