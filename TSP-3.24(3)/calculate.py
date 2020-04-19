#!/usr/bin/python
import math
import numpy as np


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
    #	print(UTMEasting)
    #	print(UTMNorthing)
    return UTMEasting, UTMNorthing


def Shrink(offset_width, *p):
    P_x = []
    P_y = []
    len_mark = len(p)
    line = []
    # 求解偏移直线的a、b、c。 ax+by=c，由所述的截距式转换而来。

    for m in range(len_mark - 1):
        dx = p[m + 1][0] - p[m][0]
        dy = p[m + 1][1] - p[m][1]
        c1 = p[m + 1][0] * p[m][1] - p[m][0] * p[m + 1][1]
        L = ((p[m + 1][0] - p[m][0]) ** 2 + (p[m + 1][1] - p[m][1]) ** 2) ** .5
        c2 = L * offset_width
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
                c = p[m][0] - offset_width
            if dy < 0:
                a = 1
                b = 0
                c = p[m][0] + offset_width
        line.append([a, b, c])
    line.append(line[0])

    # 开始计算偏移直线的交点
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
