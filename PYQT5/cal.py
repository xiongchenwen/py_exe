import math
import numpy as np


# GPS转坐标
def wgs84toutm(Long, Lat):
    grid_size = 100000.0
    WGS84_A = 6378137.0
    WGS84_B = 6356752.31424518
    WGS84_F = 0.0033528107
    WGS84_E = 0.0818191908
    WGS84_EP = 0.0820944379
    UTM_K0 = 0.9996
    UTM_FE = 500000.0
    UTM_FN_N = 0.0
    UTM_FN_S = 10000000.0
    UTM_E2 = (WGS84_E * WGS84_E)
    UTM_E4 = (UTM_E2 * UTM_E2)
    UTM_E6 = (UTM_E4 * UTM_E2)
    UTM_EP2 = (UTM_E2 / (1 - UTM_E2))
    RADIANS_PER_DEGREE = math.pi / 180
    a = WGS84_A
    eccSquared = UTM_E2
    k0 = UTM_K0

    # Make sure the longitude is between -180.00 .. 179.9
    LongTemp = (Long + 180) - int((Long + 180) / 360) * 360 - 180

    LatRad = Lat * RADIANS_PER_DEGREE
    LongRad = LongTemp * RADIANS_PER_DEGREE

    ZoneNumber = int((LongTemp + 180) / 6) + 1

    if ((Lat >= 56.0) & (Lat < 64.0) & (LongTemp >= 3.0) & (LongTemp < 12.0)):
        ZoneNumber = 32

    # Special zones for Svalbard
    if ((Lat >= 72.0) & (Lat < 84.0)):

        if ((LongTemp >= 0.0) & (LongTemp < 9.0)):
            ZoneNumber = 31
        if ((LongTemp >= 9.0) & (LongTemp < 21.0)):
            ZoneNumber = 33
        if ((LongTemp >= 21.0) & (LongTemp < 33.0)):
            ZoneNumber = 35
        if ((LongTemp >= 33.0) & (LongTemp < 42.0)):
            ZoneNumber = 37
    LongOrigin = (ZoneNumber - 1) * 6 - 180 + 3
    LongOriginRad = LongOrigin * RADIANS_PER_DEGREE
    eccPrimeSquared = (eccSquared) / (1 - eccSquared)

    N = a / math.sqrt(1 - eccSquared * math.sin(LatRad) * math.sin(LatRad))
    T = math.tan(LatRad) * math.tan(LatRad)
    C = eccPrimeSquared * math.cos(LatRad) * math.cos(LatRad)
    A = math.cos(LatRad) * (LongRad - LongOriginRad)

    M = a * ((1 - eccSquared / 4 - 3 * eccSquared * eccSquared / 64
              - 5 * eccSquared * eccSquared * eccSquared / 256) * LatRad
             - (3 * eccSquared / 8 + 3 * eccSquared * eccSquared / 32
                + 45 * eccSquared * eccSquared * eccSquared / 1024) * math.sin(2 * LatRad)
             + (15 * eccSquared * eccSquared / 256
                + 45 * eccSquared * eccSquared * eccSquared / 1024) * math.sin(4 * LatRad)
             - (35 * eccSquared * eccSquared * eccSquared / 3072) * math.sin(6 * LatRad))
    UTMEasting = k0 * N * (A + (1 - T + C) * A * A * A / 6 + (5 - 18 * T + T * T + 72 * C - 58 * eccPrimeSquared) \
                           * A * A * A * A * A / 120) + 500000.0

    UTMNorthing = k0 * (M + N * math.tan(LatRad) * (A * A / 2 + (5 - T + 9 * C + 4 * C * C) * A * A * A * A / 24 + \
                                                    (
                                                            61 - 58 * T + T * T + 600 * C - 330 * eccPrimeSquared) * A * A * A * A * A * A / 720))

    if (Lat < 0):
        # 10000000 meter offset for southern hemisphere-0
        UTMNorthing += 10000000.0
    UTMNorthing = UTMNorthing - 3373400
    UTMEasting = UTMEasting - 245000
    # print(UTMEasting)
    # print(UTMNorthing)
    return UTMEasting, UTMNorthing


# 多边形偏置算法部分
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

    # 解决多边形偏置过程中环自交问题，
    # 求每一条边与左右边的交点，通过判断x坐标点（或者y坐标点）的大小，判断是否自交
    # 其中有4个不同的情况（边与x轴平行时，边与y轴平行时）可参考上面论文理解
    # 将每一条边加入判断
    for i in range(0, len(line)):
        Px = []
        Py = []
        line_1 = []
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
