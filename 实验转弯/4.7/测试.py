import math
O1 = [80, 100]
O2 = [60, 110]
degree2 = math.degrees(math.atan((O1[1] - O2[1]) / (O1[0] - O2[0])))
print('degree2', degree2)