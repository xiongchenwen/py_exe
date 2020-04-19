# 使用说明
# 程序运行后，通过鼠标选点进行画图（左键选点，右键取消）
# POINTNUM表示选择的顶点数目
# 扫描填充算法详解：https://blog.csdn.net/wodownload2/article/details/52154207?utm_source=distribute.pc_relevant.none-task


import matplotlib.pyplot as plt

# 多边形顶点数
POINTNUM = 6
# 分辨率
LENGTH = 60

fig = plt.figure("扫描线填充算法  (使用方法：在图中随机选取6个点)", figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.axis([0, LENGTH, 0, LENGTH])

path_width = 3


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


points = [None] * POINTNUM


def polyScan():
    MaxY = 0
    MinY = LENGTH
    for i in range(POINTNUM):
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
        for j in range(POINTNUM):  # j为各顶点序号
            if points[j].y == i:
                print('points[j].y', points[j].y)
                # 一个点跟前面的一个点形成一条线段，跟后面的点也形成线段
                # 如果points[j].y较小就加入
                if points[(j - 1 + POINTNUM) % POINTNUM].y > points[j].y:
                    p = XET()
                    p.x = points[j].x
                    p.ymax = points[(j - 1 + POINTNUM) % POINTNUM].y
                    p.dx = (points[(j - 1 + POINTNUM) % POINTNUM].x - points[j].x) / (
                            points[(j - 1 + POINTNUM) % POINTNUM].y - points[j].y)
                    p.next = NET[i].next
                    NET[i].next = p
                    # print('j', j)

                if points[(j + 1 + POINTNUM) % POINTNUM].y > points[j].y:
                    p = XET()
                    p.x = points[j].x
                    p.ymax = points[(j + 1 + POINTNUM) % POINTNUM].y
                    p.dx = (points[(j + 1 + POINTNUM) % POINTNUM].x - points[j].x) / (
                            points[(j + 1 + POINTNUM) % POINTNUM].y - points[j].y)
                    p.next = NET[i].next
                    NET[i].next = p
                    # print('j', j)
                print('i', i)

    # print('AET',AET)
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
        # 配对填充颜色,得到了扫描线与多边形的交点
        if i == a:
            p = AET.next
            while p and p.next:
                j_1 = p.x
                # print('j_1',j_1)
                # y = i
                j_2 = p.next.x
                X = [j_1, j_2]
                Y = [i, i]
                # print('x', X)
                # print('Y', Y)
                plt.plot(X, Y, color='red', linewidth=0.5)

                # 考虑端点情况
                p = p.next.next
                # print('a', a)
            a += path_width


# 这里是画板取点，后面程序中没有加入
def paint():
    # 取点
    pos = plt.ginput(POINTNUM)
    X = []
    Y = []
    for i in range(POINTNUM):
        x = int(pos[i][0])
        y = int(pos[i][1])
        X.append(x)
        Y.append(y)
        points[i] = Point(x, y)
    X.append(int(pos[0][0]))
    Y.append(int(pos[0][1]))
    plt.plot(X, Y, color='red', linewidth=1)
    polyScan()
    plt.show()


if __name__ == "__main__":
    paint()
