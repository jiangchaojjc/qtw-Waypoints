#coding=utf-8
from ui_main import *

def points_in_rectangle(p):
    i = 1
    point1_x = 0
    point2_x = 0
    point3_x = 0
    point4_x = 0
    point1_y = 0
    point2_y = 0
    point3_y = 0
    point4_y = 0
    point_x = []
    point_y = []

    threshold_x=float(p[1][0])-float(p[0][0])
    threshold_y=float(p[1][1]) - float(p[0][1])
    #print(threshold_x,threshold_y)

    if p[0][2] == '0' or p[0][2] == '3.14':
        direction3 = str(abs(float(p[0][2])-3.14))

        direction = [p[0][2],p[0][2],direction3,direction3]

    else:
        direction3 = str(float(p[0][2]) *(-1))
        direction = [p[0][2],p[0][2],direction3,direction3]
    #print(direction)
    if ((p[0][2] == '0' or p[0][2] == '-1.57') and (threshold_y < 0)) or ((p[0][2] == '3.14' or p[0][2] == '1.57') and (threshold_y > 0)):
        turn = ['ST', 'R2', 'ST', 'L2']
    else:
        turn = ['ST', 'L2', 'ST', 'R2']
    #print(turn)
    # run along with x axis
    if abs(threshold_y)-abs(threshold_x)< 0:
        if threshold_y < 0:
            threshold = -0.5
        else:
            threshold = 0.5
        nums = int(abs(threshold_y))*4
        #nums = (int(abs(threshold_y) // abs(threshold)//4)*8)
        #print(nums)
        points = []
        if threshold_x > 0:
            point1_x = p[0][0]
            point2_x = str(round((float(p[1][0]) - 0.3),2))
            point3_x = p[1][0]
            point4_x = str(round((float(p[0][0]) + 0.3),2))

        elif threshold_x < 0:
            point1_x = p[0][0]
            point2_x = str(round((float(p[1][0]) + 0.3),2))
            point3_x = p[1][0]
            point4_x = str(round((float(p[0][0]) - 0.3),2))
        point_x.append(point1_x)
        point_x.append(point2_x)
        point_x.append(point3_x)
        point_x.append(point4_x)

        for num in range(nums-1):
            points.append((point_x[i],str(float(p[0][1])+threshold*((num+1)//2)),direction[i],turn[i],'0','0'))
            i = i + 1
            if i ==4:
                i = 0
        points.append((p[0][0],str(float(p[0][1])+threshold*((nums+1)//2)),p[0][2],'ST','0','0'))

    else:
        # run along with y axis
        if threshold_x < 0:
            threshold = -0.5
        else:
            threshold = 0.5
        nums = int(abs(threshold_x)) * 4
        #print(nums)
        points = []
        if threshold_y > 0:
            point1_y = p[0][1]
            point2_y = str(round((float(p[1][1]) - 0.3),2))
            point3_y = p[1][1]
            point4_y = str(round((float(p[0][1]) + 0.3),2))
        if threshold_y < 0:
            point1_y = p[0][1]
            point2_y = str(round((float(p[1][1]) + 0.3),2))
            point3_y = p[1][1]
            point4_y = str(round((float(p[0][1]) - 0.3),2))
        point_y.append(point1_y)
        point_y.append(point2_y)
        point_y.append(point3_y)
        point_y.append(point4_y)
        for num in range(nums-1):
            points.append((str(float(p[0][0])+threshold*((num+1)//2)),point_y[i],direction[i],turn[i],'0','0'))

            i = i + 1
            if i ==4:
                i = 0
        points.append((str(float(p[0][0])+threshold*((nums+1)//2)),p[0][1],p[0][2],'ST','0','0'))
    points.append((p[1][0],p[1][1],p[1][2],p[1][3],'0','0'))
    return points