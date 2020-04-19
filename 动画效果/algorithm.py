import math


def polyScan(point_1, point_offset, path_width, angle):
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
    POINTNUM_1 = len(point_offset)
    points = [None] * POINTNUM_1
    top_list = []
    low_list = []
    # 多边形顺时针旋转
    b = max(point_1[1])  # 绕(b,b)旋转,b为y轴最大值，步进旋转法中用到，在此程序中不能出现坐标y为负数，所以取较大者为旋转中心点
    # angle = 0  # 初始旋转角度
    # print('b', b)
    distance_set = []
    # 步进旋转法，参考论文（复杂边界田块多旋翼无人机自主作业路径规划）
    # for i in range(0, 180):
    #     if angle <= 180:
    radian = math.radians(angle)  # 角度转弧度
    # 坐标旋转公式
    Polygon_1 = point_1
    for i in range(POINTNUM_1):
        x = (Polygon_1[i][0])
        y = (Polygon_1[i][1])
        x_1 = int(((x - b) * math.cos(-radian) - (y - b) * math.sin(-radian) + b) * 10)
        y_1 = int(((y - b) * math.cos(-radian) + (x - b) * math.sin(-radian) + b) * 10)
        points[i] = Point(x_1, y_1)

    # 扫描线算法求解
    MaxY = 0
    MinY = float("inf")  # float("inf") 表示正无穷
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
        # 计算扫描线角度在（0-180）之间的路线距离，求出最小值
        if i == c:
            p = AET.next
            while p and p.next:
                top = []
                low = []
                j_1 = p.x / 10
                j_2 = p.next.x / 10
                distance = j_2 - j_1
                t_distance += distance

                # low.append(j_1)
                # low.append(i/10)
                # top.append(j_2)
                # top.append(i/10)
                # low_list.append(low)
                # top_list.append(top)

                # 考虑端点情况
                p = p.next.next
            c += path_width
    return t_distance
            # distance_set.append(t_distance)
            # angle += 1
            # print('总距离', round(t_distance, 3))  # round 保留3位小数
        # else:
        #     pass
    #     print('angle', angle-1)
    # print('distance_set', distance_set)
    # min_angle = distance_set.index(min(distance_set))  # 求最小值在列表中位置，得到的数据其实就是角度大小
    # min_distance = min(distance_set)  # 最短距离
    # return min_angle, min_distance


def polyScan_Draw(point_1, point_offset, path_width, min_angle):
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
    # min_angle, min_distance = polyScan(point_1, point_offset, path_width)
    POINTNUM_1 = len(point_offset)
    points = [None] * POINTNUM_1
    # 多边形顺时针旋转
    b = max(point_1[1])  # 绕(b,b)旋转,b为y轴最大值，步进旋转法中用到，在此程序中不能出现坐标y为负数，所以取较大者为旋转中心点
    #################################################################################
    # 此次算法重复上面，
    # 只是在最后加上画图。（应该程序可以精简，暂时未解决）
    radian = math.radians(min_angle)  # 角度转弧度
    Polygon_1 = point_offset
    for i in range(POINTNUM_1):
        x = (Polygon_1[i][0])
        y = (Polygon_1[i][1])
        x_1 = int(((x - b) * math.cos(-radian) - (y - b) * math.sin(-radian) + b) * 10)
        y_1 = int(((y - b) * math.cos(-radian) + (x - b) * math.sin(-radian) + b) * 10)
        points[i] = Point(x_1, y_1)

    MaxY = 0
    MinY = float("inf")
    for i in range(POINTNUM_1):
        if points[i].y > MaxY:
            MaxY = points[i].y
        if points[i].y < MinY:
            MinY = points[i].y

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
    boundary_point = []
    route_point = []
    top_list = []
    low_list = []
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
        # 画图部分（多边形内扫描线）
        # 配对填充颜色
        if i == a:
            p = AET.next
            while p and p.next:
                boundary_point_ = []
                X_1 = []
                Y_1 = []
                j_1 = p.x / 10
                j_2 = p.next.x / 10
                x_1 = ((j_1 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_1 = ((j_1 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                x_2 = ((j_2 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_2 = ((j_2 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)

                X_1.append(x_1)
                X_1.append(x_2)
                Y_1.append(y_1)
                Y_1.append(y_2)
                boundary_point_.append(X_1)
                boundary_point_.append(Y_1)
                boundary_point.append(boundary_point_)

                # 考虑端点情况
                p = p.next.next
            a += path_width

        # 画车辆行驶路线
        if i == c:
            p = AET.next
            while p and p.next:
                top = []
                low = []
                route_point_ = []
                X_2 = []
                Y_2 = []
                j_1 = p.x / 10
                j_2 = p.next.x / 10
                x_1 = ((j_1 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_1 = ((j_1 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                x_2 = ((j_2 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
                y_2 = ((j_2 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
                X_2.append(x_1)
                X_2.append(x_2)
                Y_2.append(y_1)
                Y_2.append(y_2)
                route_point_.append(X_2)
                route_point_.append(Y_2)
                route_point.append(route_point_)

                # print('X_2', X_2)
                # print('Y_2', Y_2)
                low.append(j_1)
                low.append(i / 10)
                top.append(j_2)
                top.append(i / 10)
                low_list.append(low)
                top_list.append(top)
                # 考虑端点情况
                p = p.next.next
            c += path_width
            # print('low_list', low_list)
            # print('top_list', top_list)

    # print('boundary_point', boundary_point)
    # print('route_point', route_point)
    return boundary_point, route_point, top_list, low_list, b


# ##################################################################################
# def Rec_turn_point(point_1, point_offset, path_width, min_angle):
#     # 定义边的结构
#     class XET:
#         def __init__(self, x=0.0, dx=0.0, ymax=0):
#             self.x = x
#             self.dx = dx
#             self.ymax = ymax
#             self.next = None
#
#     class Point:
#         def __init__(self, x, y):
#             self.x = x
#             self.y = y
#
#     POINTNUM_1 = len(point_offset)
#     points = [None] * POINTNUM_1
#     top_list = []
#     low_list = []
#     # 多边形顺时针旋转
#     b = max(point_1[1])  # 绕(b,b)旋转,b为y轴最大值，步进旋转法中用到，在此程序中不能出现坐标y为负数，所以取较大者为旋转中心点
#     #################################################################################
#     # 此次算法重复上面，
#     # 只是在最后加上画图。（应该程序可以精简，暂时未解决）
#     radian = math.radians(min_angle)  # 角度转弧度
#     Polygon_1 = point_offset
#     for i in range(POINTNUM_1):
#         x = (Polygon_1[i][0])
#         y = (Polygon_1[i][1])
#         x_1 = int(((x - b) * math.cos(-radian) - (y - b) * math.sin(-radian) + b) * 10)
#         y_1 = int(((y - b) * math.cos(-radian) + (x - b) * math.sin(-radian) + b) * 10)
#         points[i] = Point(x_1, y_1)
#
#     MaxY = 0
#     MinY = float("inf")
#     for i in range(POINTNUM_1):
#         if points[i].y > MaxY:
#             MaxY = points[i].y
#         if points[i].y < MinY:
#             MinY = points[i].y
#
#     c = MinY + path_width / 2
#     # 总距离
#     t_distance = 0
#     # 初始化AET表
#     AET = XET()
#     # 初始化NET表
#     NET = [None] * (MaxY + 1)
#     for i in range(MaxY + 1):
#         NET[i] = XET()
#
#     # 扫描并建立NET表
#     for i in range(MaxY + 1):  # i为y坐标
#         for j in range(POINTNUM_1):  # j为各顶点序号
#             if points[j].y == i:
#                 # 一个点跟前面的一个点形成一条线段，跟后面的点也形成线段
#                 # 如果points[j].y较小就加入
#                 if points[(j - 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
#                     p = XET()
#                     p.x = points[j].x
#                     p.ymax = points[(j - 1 + POINTNUM_1) % POINTNUM_1].y
#                     p.dx = (points[(j - 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
#                             points[(j - 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
#                     p.next = NET[i].next
#                     NET[i].next = p
#
#                 if points[(j + 1 + POINTNUM_1) % POINTNUM_1].y > points[j].y:
#                     p = XET()
#                     p.x = points[j].x
#                     p.ymax = points[(j + 1 + POINTNUM_1) % POINTNUM_1].y
#                     p.dx = (points[(j + 1 + POINTNUM_1) % POINTNUM_1].x - points[j].x) / (
#                             points[(j + 1 + POINTNUM_1) % POINTNUM_1].y - points[j].y)
#                     p.next = NET[i].next
#                     NET[i].next = p
#
#     # print('NET', NET)
#
#     # 建立并更新活性边表AET
#     for i in range(MinY, MaxY + 1):
#         # 计算新的交点x（p.x）, 更新AET
#         p = AET.next
#         while p:
#             p.x = p.x + p.dx
#             p = p.next
#         # print('i', i)
#         # 更新后新AET先排序
#         # 断表排序, 不再开辟空间
#         tq = AET
#         p = AET.next
#         tq.next = None  # tq中最后一个取值为None
#         while p:
#             while tq.next and p.x >= tq.next.x:
#                 tq = tq.next
#             s = p.next
#             p.next = tq.next
#             tq.next = p
#             p = s
#             tq = AET
#         # (改进算法)
#         # 先从AET表中删除ymax == i的结点
#         q = AET
#         p = q.next
#         while p:
#             if p.ymax == i:
#                 q.next = p.next  # 删除了ymax == i时的x dx ymax
#                 p = q.next
#             else:
#                 q = q.next
#                 p = q.next
#
#         # 将NET中的新点加入AET, 并用插入法按X值递增排序
#         p = NET[i].next
#         q = AET
#         while p:
#             while q.next and p.x >= q.next.x:
#                 q = q.next
#             s = p.next
#             p.next = q.next
#             q.next = p
#             p = s
#             q = AET
# ##########################################
#         # 计算转弯点坐标
#         if i == c:
#             p = AET.next
#             while p and p.next:
#                 top = []
#                 low = []
#                 j_1 = p.x / 10
#                 j_2 = p.next.x / 10
#                 # x_1 = ((j_1 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
#                 # y_1 = ((j_1 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
#                 # x_2 = ((j_2 - b) * math.cos(radian) - (i / 10 - b) * math.sin(radian) + b)
#                 # y_2 = ((j_2 - b) * math.sin(radian) + (i / 10 - b) * math.cos(radian) + b)
#                 # if y_1 > y_2:
#                 #     x = x_2
#                 #     x_2 = x_1
#                 #     x_1 = x
#                 #     y = y_2
#                 #     y_2 = y_1
#                 #     y_1 = y
#                 # else:
#                 #     pass
#                 low.append(j_1)
#                 low.append(i/10)
#                 top.append(j_2)
#                 top.append(i/10)
#                 low_list.append(low)
#                 top_list.append(top)
#                 # 考虑端点情况
#                 p = p.next.next
#             c += path_width
#     # print('low_list', low_list)
#     # print('top_list', top_list)
#     return top_list, low_list, b
