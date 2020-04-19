import math
import numpy as np

import algorithm


# 圆弧函数
def arc(r, angle_0, angle_1, xin_x, xin_y):
    # print('angle_0', angle_0)
    angle_list = [math.radians(x) for x in np.arange(angle_0, angle_1)]
    angle_list.append(math.radians(angle_1))
    # print('angle_list', math.degrees(angle_list))
    x_list = [xin_x + r * math.cos(x) for x in angle_list]
    y_list = [xin_y + r * math.sin(x) for x in angle_list]
    return x_list, y_list

# O1 = [A[0] + turn_r * math.sin(radian1), A[1] - turn_r * math.cos(radian1)]
# O2 = [B[0] - turn_r * math.sin(radian1), B[1] + turn_r * math.cos(radian1)]
# O1 = [A[0] + turn_r, A[1]]
# O2 = [B[0] - turn_r, B[1]]

##########################################################################################
# 各类转弯方式计算。
def U_turn(A, B, turn_r, TOP_EDGE, min_angle):
    print('A', A)
    print('B', B)
    radian1 = math.radians(min_angle)
    # print('min_angle', min_angle)
    if TOP_EDGE:
        print('1111')
        O1 = [A[0] + turn_r * math.sin(radian1), A[1] - turn_r * math.cos(radian1)]
        O2 = [B[0] - turn_r * math.sin(radian1), B[1] + turn_r * math.cos(radian1)]
        # O1 = [A[0] + turn_r, A[1]]
        # O2 = [B[0] - turn_r, B[1]]
        print('O1', O1)
        print('O2', O2)
        degree2 = math.degrees(math.atan((O1[1] - O2[1]) / (O1[0] - O2[0])))
        print('degree2', degree2)
        radian2 = math.radians(degree2)
        if O1[1] < O2[1]:   # [Y1<Y2]
            if O1[0] < O2[0]:
                H1 = [O1[0] - turn_r * math.sin(radian2), O1[1] + turn_r * math.cos(radian2)]
                H2 = [O2[0] - turn_r * math.sin(radian2), O2[1] + turn_r * math.cos(radian2)]
                arc1 = arc(turn_r, degree2 + 90, 90 + min_angle, O1[0], O1[1])
                arc2 = arc(turn_r, min_angle - 90, degree2 + 90, O2[0], O2[1])
            else:  
                H1 = [O1[0] + turn_r * math.sin(radian2), O1[1] - turn_r * math.cos(radian2)]
                H2 = [O2[0] + turn_r * math.sin(radian2), O2[1] - turn_r * math.cos(radian2)]
                print('H1', H1)
                print('H2', H2)
                arc1 = arc(turn_r, 270 + degree2, 90 + min_angle, O1[0], O1[1])
                arc2 = arc(turn_r, min_angle - 90, 270 + degree2, O2[0], O2[1])

        else:  # [Y1>Y2]
            if O1[0] > O2[0]:
                radian2 = math.radians(degree2)
                H1 = [O1[0] + turn_r * math.sin(radian2), O1[1] - turn_r * math.cos(radian2)]
                H2 = [O2[0] + turn_r * math.sin(radian2), O2[1] - turn_r * math.cos(radian2)]
                arc1 = arc(turn_r, degree2 - 90, min_angle + 90, O1[0], O1[1])
                arc2 = arc(turn_r, min_angle - 90, degree2 - 90, O2[0], O2[1])
            else:
                H1 = [O1[0] - turn_r * math.sin(radian2), O1[1] + turn_r * math.cos(radian2)]
                H2 = [O2[0] - turn_r * math.sin(radian2), O2[1] + turn_r * math.cos(radian2)]
                print('111')
                print('H1', H1)
                print('H2', H2)
                arc1 = arc(turn_r, 90 + degree2, 90 + min_angle, O1[0], O1[1])
                arc2 = arc(turn_r, 90 - min_angle, 90 + degree2, O2[0], O2[1])


        # print('degree1', degree1)
        # degree2 = degree1 + 90
        # radian2 = math.radians(degree2)
        # # print('degree2', degree2)
        # H1 = [O1[0] - turn_r * math.sin(radian2), O1[1] + turn_r * math.cos(radian2)]
        # H2 = [O2[0] - turn_r * math.sin(radian2), O2[1] + turn_r * math.cos(radian2)]
        # print('H1', H1)
        # arc1 = arc(turn_r, degree2+90, 180-degree3, O1[0], O1[1])
        arc1[0].reverse()
        arc1[1].reverse()
        # arc2 = arc(turn_r, -degree3, degree2+90, O2[0], O2[1])
        arc2[0].reverse()
        arc2[1].reverse()
        line_x = [H1[0], H2[0]]
        line_y = [H1[1], H2[1]]
        x = arc1[0] + line_x + arc2[0]
        y = arc1[1] + line_y + arc2[1]
    else:
        O1 = [A[0] + turn_r * math.sin(radian1), A[1] - turn_r * math.cos(radian1)]
        O2 = [B[0] - turn_r * math.sin(radian1), B[1] + turn_r * math.cos(radian1)]
        print('O1', O1)
        print('O2', O2)
        # O1 = [A[0] + turn_r, A[1]]
        # O2 = [B[0] - turn_r, B[1]]
        degree2 = math.degrees(math.atan((O1[1] - O2[1]) / (O1[0] - O2[0])))
        radian2 = math.radians(degree2)
        print('degree2', degree2)
        if O1[1] < O2[1]:
            if O1[0] > O2[0]:
                H1 = [O1[0] - turn_r * math.sin(radian2), O1[1] - turn_r * math.cos(radian2)]
                H2 = [O2[0] - turn_r * math.sin(radian2), O2[1] - turn_r * math.cos(radian2)]
                arc1 = arc(turn_r, min_angle - 270, 90 + degree2, O1[0], O1[1])
                arc2 = arc(turn_r, 90 + degree2, min_angle - 90, O2[0], O2[1])
            else:
                H1 = [O1[0] + turn_r * math.sin(radian2), O1[1] - turn_r * math.cos(radian2)]
                H2 = [O2[0] + turn_r * math.sin(radian2), O2[1] - turn_r * math.cos(radian2)]
                arc1 = arc(turn_r, 90 + min_angle, 270 + degree2, O1[0], O1[1])
                arc2 = arc(turn_r, 270 + degree2, 270 + min_angle, O2[0], O2[1])


        else:
            if O1[0] > O2[0]:
                H1 = [O1[0] - turn_r * math.sin(radian2), O1[1] + turn_r * math.cos(radian2)]
                H2 = [O2[0] - turn_r * math.sin(radian2), O2[1] + turn_r * math.cos(radian2)]
                print('H1', H1)
                print('H2', H2)
                arc1 = arc(turn_r, 90 + min_angle, 90 + degree2, O1[0], O1[1])
                arc2 = arc(turn_r, degree2 + 90, 270 + min_angle, O2[0], O2[1])
            else:
                H1 = [O1[0] + turn_r * math.sin(radian2), O1[1] - turn_r * math.cos(radian2)]
                H2 = [O2[0] + turn_r * math.sin(radian2), O2[1] - turn_r * math.cos(radian2)]
                print('H1', H1)
                print('H2', H2)
                arc1 = arc(turn_r, 90 + min_angle, 270 + degree2, O1[0], O1[1])
                arc2 = arc(turn_r, degree2 + 270, min_angle+270, O2[0], O2[1])


        line_x = [H1[0], H2[0]]
        line_y = [H1[1], H2[1]]
        x = arc1[0] + line_x + arc2[0]
        y = arc1[1] + line_y + arc2[1]
    print('x', x)
    print('y', y)
    return [x, y]


def U2_turn(A, B, turn_r, TOP_EDGE):
    # print('A', A)
    # print('B', B)
    print('turn_r', turn_r)
    print('TOP_EDGE', TOP_EDGE)
    if TOP_EDGE:
        O1 = [A[0] + turn_r, A[1]]
        O2 = [B[0] - turn_r, B[1]]
        O3 = []
        h = O2[1] - O1[1]
        if A[1] >= B[1]:
            B2 = [B[0], A[1]]
            O3 = O1
            line1 = [[B[0], B[0]], [B[1], B2[1]]]
            arc1 = arc(turn_r, 0, 180, O3[0], O3[1])
            arc1[0].reverse()
            arc1[1].reverse()
            x = arc1[0] + line1[0]
            y = arc1[1] + line1[1]
        else:
            A2 = [A[0], B[1]]
            O3 = O2
            line1 = [[A[0], A[0]], [A[1], A2[1]]]
            arc1 = arc(turn_r, 0, 180, O3[0], O3[1])
            x = line1[0] + arc1[0]
            y = line1[1] + arc1[1]
    else:
        O1 = [A[0] + turn_r, A[1]]
        O2 = [B[0] - turn_r, B[1]]
        O3 = []
        h = O2[1] - O1[1]
        if A[1] >= B[1]:
            A2 = [A[0], B[1]]
            O3 = O2
            line1 = [[A[0], A[0]], [A[1], A2[1]]]
            arc1 = arc(turn_r, 180, 360, O3[0], O3[1])
            x = line1[0] + arc1[0]
            y = line1[1] + arc1[1]
        else:
            B2 = [B[0], A[1]]
            O3 = O1
            line1 = [[B[0], B[0]], [B[1], B2[1]]]
            arc1 = arc(turn_r, 180, 360, O3[0], O3[1])
            x = arc1[0] + line1[0]
            y = arc1[1] + line1[1]
    # print('x', x)
    # print('y', y)     #############################################
    return [x, y]


# "Ω"型转弯
def O_turn(A, B, turn_r, TOP_EDGE):
    if TOP_EDGE:
        O1 = [A[0] - turn_r, A[1]]
        O2 = [B[0] + turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O1O2 = round(O1O2, 6)
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        degree2 = degree1 + 90
        radian2 = math.radians(degree2)
        O3 = [C[0] + O3C * math.cos(radian2), C[1] + O3C * math.sin(radian2)]
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [(O3[0] + O1[0]) / 2, (O3[1] + O1[1]) / 2]
        H2 = [(O3[0] + O2[0]) / 2, (O3[1] + O2[1]) / 2]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        degreeO312 = math.degrees(math.atan(O3C / (O1O2 / 2)))
        degree3 = degree1 + degreeO312
        degree4 = 180 - (degreeO312 - degree1)
        degree5 = 180 + degree3
        degree6 = 180 + degree4
        arc1_x, arc1_y = arc(turn_r, 0, degree3, O1[0], O1[1])
        arc2_x, arc2_y = arc(turn_r, degree4, 180, O2[0], O2[1])
        arc3_x, arc3_y = arc(turn_r, 0, degree5, O3[0], O3[1])
        arc3_x.reverse()
        arc3_y.reverse()
        arc4_x, arc4_y = arc(turn_r, degree6, 360, O3[0], O3[1])
        arc4_x.reverse()
        arc4_y.reverse()
        x = arc1_x + arc3_x + arc4_x + arc2_x
        y = arc1_y + arc3_y + arc4_y + arc2_y
    else:
        O1 = [A[0] - turn_r, A[1]]
        O2 = [B[0] + turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        degree2 = degree1 + 270
        radian2 = math.radians(degree2)
        O3 = [C[0] + O3C * math.cos(radian2), C[1] + O3C * math.sin(radian2)]
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [(O3[0] + O1[0]) / 2, (O3[1] + O1[1]) / 2]
        H2 = [(O3[0] + O2[0]) / 2, (O3[1] + O2[1]) / 2]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        degreeO312 = math.degrees(math.atan(O3C / (O1O2 / 2)))
        degree3 = 360 - (degreeO312 - degree1)
        degree4 = 180 + degreeO312 + degree1
        degree5 = 180 - (degreeO312 - degree1)
        degree6 = degreeO312 + degree1
        arc1_x, arc1_y = arc(turn_r, degree3, 360, O1[0], O1[1])
        arc1_x.reverse()
        arc1_y.reverse()
        arc2_x, arc2_y = arc(turn_r, 180, degree4, O2[0], O2[1])
        arc2_x.reverse()
        arc2_y.reverse()
        arc3_x, arc3_y = arc(turn_r, degree5, 360, O3[0], O3[1])
        arc4_x, arc4_y = arc(turn_r, 0, degree6, O3[0], O3[1])
        x = arc1_x + arc3_x + arc4_x + arc2_x
        y = arc1_y + arc3_y + arc4_y + arc2_y
    return [x, y]


# "T"型转弯
def T_turn(A, B, turn_r, TOP_EDGE):
    if TOP_EDGE:
        O1 = [A[0] + turn_r, A[1]]
        O2 = [B[0] - turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O1[0] - O2[0]) ** 2 + (O1[1] - O2[1]) ** 2) ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan(abs(O1[1] - O2[1]) / (O1[0] - O2[0])))
        degree2 = 90 - degree1
        radian2 = math.radians(degree2)
        O3 = [C[0] + O3C * math.cos(radian2), C[1] + O3C * math.sin(radian2)]
        degreeO321 = math.degrees(math.atan(O3C / (O1O2 / 2)))
        degree3 = degreeO321 - degree1
        degree4 = 180 - (degree1 + degreeO321)
        degree5 = 180 + degree3
        degree6 = 180 + degree4
        H1 = [(O1[0] + O3[0]) / 2, (O1[1] + O3[1]) / 2]
        H2 = [(O2[0] + O3[0]) / 2, (O2[1] + O3[1]) / 2]
        arc1_x, arc1_y = arc(turn_r, degree4, 180, O1[0], O1[1])
        arc2_x, arc2_y = arc(turn_r, 0, degree3, O2[0], O2[1])
        arc3_x, arc3_y = arc(turn_r, degree5, degree6, O3[0], O3[1])
        x = arc1_x + arc3_x + arc2_x
        y = arc1_y + arc3_y + arc2_y
    else:
        O1 = [A[0] + turn_r, A[1]]
        O2 = [B[0] - turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O1[0] - O2[0]) ** 2 + (O1[1] - O2[1]) ** 2) ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan(abs(O1[1] - O2[1]) / (O1[0] - O2[0])))
        degree2 = 180 + 90 - degree1
        radian2 = math.radians(degree2)
        O3 = [C[0] + O3C * math.cos(radian2), C[1] + O3C * math.sin(radian2)]
        degreeO321 = math.degrees(math.atan(O3C / (O1O2 / 2)))
        degree3 = 180 + degreeO321 - degree1
        degree4 = 360 - degreeO321 - degree1
        degree5 = degreeO321 - degree1
        degree6 = 180 - degreeO321 - degree1
        H1 = [(O1[0] + O3[0]) / 2, (O1[1] + O3[1]) / 2]
        H2 = [(O2[0] + O3[0]) / 2, (O2[1] + O3[1]) / 2]
        arc1_x, arc1_y = arc(turn_r, 180, degree3, O1[0], O1[1])
        arc2_x, arc2_y = arc(turn_r, degree4, 360, O2[0], O2[1])
        arc3_x, arc3_y = arc(turn_r, degree5, degree6, O3[0], O3[1])
        x = arc1_x + arc3_x + arc2_x
        y = arc1_y + arc3_y + arc2_y
    return [x, y]


# T' turn
def T2_turn(A, B, turn_r, TOP_EDGE):
    if TOP_EDGE:
        O1 = [A[0] + turn_r, A[1]]
        O2 = [B[0] - turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan(abs(O2[1] - O1[1]) / abs(O2[0] - O1[0])))
        degree2 = 90 - degree1
        radian2 = math.radians(degree2)
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [O1[0] + turn_r * math.cos(radian2), O1[1] + turn_r * math.sin(radian2)]
        H2 = [O2[0] + turn_r * math.cos(radian2), O2[1] + turn_r * math.sin(radian2)]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        arc1 = arc(turn_r, degree2, 180, O1[0], O1[1])
        arc1[0].reverse()
        arc1[1].reverse()
        arc2 = arc(turn_r, 0, degree2, O2[0], O2[1])
        arc2[0].reverse()
        arc2[1].reverse()
        t_line = [[H1[0], H2[0]], [H1[1], H2[1]]]
        x = arc1[0] + t_line[0] + arc2[0]
        y = arc1[1] + t_line[1] + arc2[1]
    else:
        O1 = [A[0] + turn_r, A[1]]
        O2 = [B[0] - turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan(abs(O2[1] - O1[1]) / abs(O2[0] - O1[0])))
        degree2 = 180 + 90 - degree1
        radian2 = math.radians(degree2)
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [O1[0] + turn_r * math.cos(radian2), O1[1] + turn_r * math.sin(radian2)]
        H2 = [O2[0] + turn_r * math.cos(radian2), O2[1] + turn_r * math.sin(radian2)]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        arc1 = arc(turn_r, 180, degree2, O1[0], O1[1])
        arc2 = arc(turn_r, degree2, 360, O2[0], O2[1])
        l_line = [[H1[0], H2[0]], [H1[1], H2[1]]]
        x = arc1[0] + l_line[0] + arc2[0]
        y = arc1[1] + l_line[1] + arc2[1]
    return [x, y]


# 只有直线倒车特性
def M_turn(A, B, turn_r, TOP_EDGE):
    if TOP_EDGE:
        O1 = [A[0] - turn_r, A[1]]
        O2 = [B[0] + turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        degree2 = degree1 + 90
        radian2 = math.radians(degree2)
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [O1[0] + turn_r * math.cos(radian2), O1[1] + turn_r * math.sin(radian2)]
        H2 = [O2[0] + turn_r * math.cos(radian2), O2[1] + turn_r * math.sin(radian2)]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        arc1 = arc(turn_r, 0, degree2, O1[0], O1[1])
        arc2 = arc(turn_r, degree2, 180, O2[0], O2[1])
        t_line = [[H1[0], H2[0]], H1[1], H2[1]]
        x = arc1[0] + t_line[0] + arc2[0]
        y = arc1[1] + t_line[1] + arc2[1]
    else:
        O1 = [A[0] - turn_r, A[1]]
        O2 = [B[0] + turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        degree2 = degree1 + 270
        radian2 = math.radians(degree2)
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [O1[0] + turn_r * math.cos(radian2), O1[1] + turn_r * math.sin(radian2)]
        H2 = [O2[0] + turn_r * math.cos(radian2), O2[1] + turn_r * math.sin(radian2)]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        arc1 = arc(turn_r, degree2, 360, O1[0], O1[1])
        arc2 = arc(turn_r, 180, degree2, O2[0], O2[1])
        l_line = [[H1[0], H2[0]], [H1[1], H2[1]]]
        x = arc1[0] + l_line[0] + arc2[0]
        y = arc1[1] + l_line[1] + arc2[1]
    return [x, y]


# 有转弯倒车特性
def M2_turn(A, B, turn_r, TOP_EDGE):
    if TOP_EDGE:
        O1 = [A[0] - turn_r, A[1]]
        O2 = [B[0] + turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        tran = (O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2
        O1O2 = tran ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        degree2 = degree1 + 90
        radian2 = math.radians(degree2)
        O3 = [C[0] + O3C * math.cos(radian2), C[1] + O3C * math.sin(radian2)]
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [(O3[0] + O1[0]) / 2, (O3[1] + O1[1]) / 2]
        H2 = [(O3[0] + O2[0]) / 2, (O3[1] + O2[1]) / 2]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        degreeO312 = math.degrees(math.atan(O3C / (O1O2 / 2)))
        degree3 = degree1 + degreeO312
        degree4 = 180 - (degreeO312 - degree1)
        degree5 = 180 + degree3
        degree6 = 180 + degree4
        arc1_x, arc1_y = arc(turn_r, 0, degree3, O1[0], O1[1])
        arc2_x, arc2_y = arc(turn_r, degree4, 180, O2[0], O2[1])
        arc3_x, arc3_y = arc(turn_r, degree5, degree6, O3[0], O3[1])
        x = arc1_x + arc3_x + arc2_x
        y = arc1_y + arc3_y + arc2_y
    else:
        O1 = [A[0] - turn_r, A[1]]
        O2 = [B[0] + turn_r, B[1]]
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        trans = (O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2
        O1O2 = trans ** .5
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree1 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        degree2 = degree1 + 270
        radian2 = math.radians(degree2)
        O3 = [C[0] + O3C * math.cos(radian2), C[1] + O3C * math.sin(radian2)]
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        H1 = [(O3[0] + O1[0]) / 2, (O3[1] + O1[1]) / 2]
        H2 = [(O3[0] + O2[0]) / 2, (O3[1] + O2[1]) / 2]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        degreeO312 = math.degrees(math.atan(O3C / (O1O2 / 2)))
        degree3 = 360 - (degreeO312 - degree1)
        degree4 = 180 + degreeO312 + degree1
        degree5 = 180 - (degreeO312 - degree1)
        degree6 = degreeO312 + degree1
        arc1_x, arc1_y = arc(turn_r, degree3, 360, O1[0], O1[1])
        arc2_x, arc2_y = arc(turn_r, 180, degree4, O2[0], O2[1])
        arc3_x, arc3_y = arc(turn_r, degree6, degree5, O3[0], O3[1])
        x = arc2_x + arc3_x + arc1_x
        y = arc2_y + arc3_y + arc1_y
    return [x, y]


# 转弯显示功能整合数据,接收来自调度的转弯点列表，
# 选择调用相应的转弯算法，并将计算结果添加入列表。
# 将每一个转弯的返回值整合为一个列表。
# 代入数据，一个列表，以及车辆的机具特性。
# 以best_turn_list列表奇偶性分别选择相对应的上边界转弯以及下边界转弯。
# 添加一个奇偶性的变量，这样就可以引导相应的上边界转弯或下边界转弯方式选择。
def All_Turn(self, point_1, point_offset, path_width, row_list, turn_r, all_turn_name, min_angle):
    all_turn = []
    turn = 0
    top_list, low_list = algorithm.Rec_turn_point(self, point_1, point_offset, path_width)
    targ = len(row_list)
    for x in range(0, targ - 1):
        A = row_list[x]
        B = row_list[x + 1]
        if x % 2 == 0:
            TOP_EDGE = True
            # if top_list[A][0] > top_list[B][0]:
            a, b = top_list[B], top_list[A]
            # else:
            #     a, b = top_list[A], top_list[B]
            if all_turn_name[x] == "T":
                turn = T_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "T2":
                turn = T2_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "M":
                turn = M_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "M2":
                turn = M2_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "O":
                turn = O_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "U":
                turn = U_turn(a, b, turn_r, TOP_EDGE, min_angle)
            elif all_turn_name[x] == "U2":
                turn = U2_turn(a, b, turn_r, TOP_EDGE)
        else:
            TOP_EDGE = False
            # if low_list[A][0] > low_list[B][0]:
            a, b = low_list[B], low_list[A]
            # else:
            #     a, b = low_list[A], low_list[B]
            if all_turn_name[x] == "T":
                turn = T_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "T2":
                turn = T2_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "M":
                turn = M_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "M2":
                turn = M2_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "O":
                turn = O_turn(a, b, turn_r, TOP_EDGE)
            elif all_turn_name[x] == "U":
                turn = U_turn(a, b, turn_r, TOP_EDGE, min_angle)
            elif all_turn_name[x] == "U2":
                turn = U2_turn(a, b, turn_r, TOP_EDGE)
        all_turn.append(turn)
    return all_turn


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
    print('point_1', point_1)
    return point_1
