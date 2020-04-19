# "Ω"型转弯
def O_turn(A, B, turn_r, TOP_EDGE, min_angle):
    print('A', A)
    print('B', B)
    degree1 = min_angle
    print('degree1', degree1)
    if TOP_EDGE:
        O1 = [A[0] - turn_r*math.sin(min_angle), A[1] + turn_r*math.cos(min_angle)]
        O2 = [B[0] + turn_r*math.sin(min_angle), B[1] - turn_r*math.cos(min_angle)]
        print('O1', O1)
        print('O2', O2)
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O1O2 = round(O1O2, 6)
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree2 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        print('degree2', degree2)
        radian2 = math.radians(degree2)
        O3 = [C[0] - O3C * math.sin(radian2), C[1] + O3C * math.cos(radian2)]
        print('O3', O3)
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        # H1 = [(O3[0] + O1[0]) / 2, (O3[1] + O1[1]) / 2]
        # H2 = [(O3[0] + O2[0]) / 2, (O3[1] + O2[1]) / 2]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        # O1与O3角度
        degree3 = math.degrees(math.atan((O3[1] - O1[1]) / (O3[0] - O1[0])))
        # O2与O3角度
        degree4 = math.degrees(math.atan((O3[1] - O2[1]) / (O3[0] - O2[0])))
        arc1_x, arc1_y = arc(turn_r, degree1 - 90, degree3, O1[0], O1[1])
        arc2_x, arc2_y = arc(turn_r, degree4 + 180, 90 + degree1, O2[0], O2[1])
        arc3_x, arc3_y = arc(turn_r, 180 + degree3, 360 + degree4, O3[0], O3[1])
        x = arc1_x + arc3_x + arc2_x
        y = arc1_y + arc3_y + arc2_y
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
    print('x', x)
    print('y', y)
    return [x, y]


        O1 = [A[0] - turn_r * math.sin(radian1), A[1] + turn_r * math.cos(radian1)]
        O2 = [B[0] + turn_r * math.sin(radian1), B[1] - turn_r * math.cos(radian1)]
        print('O1', O1)
        print('O2', O2)
        C = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]
        O1O2 = ((O2[1] - O1[1]) ** 2 + (O2[0] - O1[0]) ** 2) ** .5
        O1O2 = round(O1O2, 6)
        O3C = ((2 * turn_r) ** 2 - (O1O2 / 2) ** 2) ** .5
        degree2 = math.degrees(math.atan((O2[1] - O1[1]) / (O2[0] - O1[0])))
        print('degree2', degree2)
        radian2 = math.radians(degree2)
        O3 = [C[0] + O3C * math.sin(radian2), C[1] - O3C * math.cos(radian2)]
        print('O3', O3)
        # 我也不知道我算H1、H2两个点有什么用，就先放这里吧。
        # H1 = [(O3[0] + O1[0]) / 2, (O3[1] + O1[1]) / 2]
        # H2 = [(O3[0] + O2[0]) / 2, (O3[1] + O2[1]) / 2]
        # degreeO1O2O3 = math.degrees(math.atan((O1O2/2)/O3_C))
        # O1与O3角度
        degree3 = math.degrees(math.atan((O3[1] - O1[1]) / (O3[0] - O1[0])))
        # O2与O3角度
        degree4 = math.degrees(math.atan((O3[1] - O2[1]) / (O3[0] - O2[0])))
        arc1_x, arc1_y = arc(turn_r, degree3 + 360, 270 + degree1, O1[0], O1[1])
        arc2_x, arc2_y = arc(turn_r, 90 + degree1, degree4 + 180,  O2[0], O2[1])
        arc3_x, arc3_y = arc(turn_r, degree4, 180 + degree3, O3[0], O3[1])
        arc3_x.reverse()
        arc3_y.reverse()
        x = arc1_x + arc3_x + arc2_x
        y = arc1_y + arc3_y + arc2_y
    print('x', x)
    print('y', y)
    return [x, y]