
import math

class Point:

    """ 该类（关于一系列的点）实现如下基本操作：
        1. 数组倒序
        2. 对三角形求直角顶点
        3. 对正方形求x坐标最小的顶点
        4. 对平行四边形求编号为0的点
        5. 对三角形顶点进行重新编号
        6. 对四边形顶点进行编号
        7. 计算斜率
        8. 平行四边形判定
        9. 由斜率求角度
        10.计算两直线夹角
        11.等腰直角三角形判定
        """
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def Reverse(self, vertex, k, m):
        """数组倒序"""
        # N=len(vertex)
        j = m
        for i in range(k, k + int((m - k + 1) / 2)):
            u = vertex[j]
            vertex[j] = vertex[i]
            vertex[i] = u
            j -= 1

    def maxDistance(self, p1, p2, p3):
        """求三角形直角边的顶点作为第一个顶点"""
        d1 = pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2)
        d2 = pow(p2.x - p3.x, 2) + pow(p2.y - p3.y, 2)
        d3 = pow(p1.x - p3.x, 2) + pow(p1.y - p3.y, 2)
        if abs(d2 - d3) < abs(d1 - d3) and abs(d2 - d3) < abs(d2 - d1):
            return p3
        elif abs(d1 - d3) < abs(d1 - d2) and abs(d1 - d3) < abs(d2 - d3):
            return p1
        else:
            return p2


    def Xmin(self, vertex):
        """寻找正方形x最小的点的下标"""
        min_index = 0
        for i in range(0, len(vertex)):
            if vertex[i].x < vertex[min_index].x:
                min_index = i
        return min_index

    def numberVertexParallelogram(self, vertex, box):
        """对平行四边形进行编号"""
        break_flag = 0
        while break_flag == 0:
            for i in range(0, 4):
                while break_flag == 0:
                    for j in range(0, 4):
                        if abs(vertex[i].x - box[j][0]) <= 10 and abs(
                                vertex[i].y - box[j][1]) <= 10:
                            vertexnum0 = i
                            break_flag = 1
        return vertexnum0

    def numberVertexTriangle(self, vertex):
        """对三角形进行编号"""
        v_rightAngle = self.maxDistance(vertex[0], vertex[1], vertex[2])
        # 前两个存斜边顶点，第三个存直角顶点,直角点存y小的
        if v_rightAngle != vertex[2]:
            if vertex[0] == v_rightAngle:
                vertex[0] = vertex[2]
            else:
                vertex[1] = vertex[2]
            vertex[2] = v_rightAngle
        if vertex[0].y > vertex[1].y:
            t = vertex[1]
            vertex[1] = vertex[0]
            vertex[0] = t

        return vertex




    def numberVertexuadrangle(self, type, vertex, box):
        """对四边形顶点进行编号"""
        if type == 0:
            vertexnum0 = self.Xmin(vertex)

        else:
            vertexnum0 = self.numberVertexParallelogram(vertex, box)
        if vertexnum0 != 0:
            self.Reverse(vertex, vertexnum0, 3)
            self.Reverse(vertex, 0, vertexnum0 - 1)
            self.Reverse(vertex, 0, 3)

        return vertex

    def getSlope(self, p1, p2, flag):
        """计算斜率
            flag: 1表示模板图"""
        if 0 <= abs(p1.x - p2.x) <= 15 and p1.y != p2.y:
            slope = float("inf")
        else:
            # 邻边斜率
            slope = ((-1) * (p1.y) + p2.y) / (p1.x - p2.x)
            if flag == 1:  # 针对电子图斜率规整的情况，0，1，-1
                if abs(slope) < 0.2:
                    slope = 0
                if abs(abs(slope) - 1) < 0.2:
                    if slope < 0:
                        slope = -1
                    else:
                        slope = 1
        return slope


    def parallelogramJudge(self, vertex):
        """平行四边形判别：两组对边分别平行的四边形是平行四边形"""
        k01 = self.getSlope(vertex[0], vertex[1], 0)
        k23 = self.getSlope(vertex[2], vertex[3], 0)
        k12 = self.getSlope(vertex[1], vertex[2], 0)
        k03 = self.getSlope(vertex[0], vertex[3], 0)
        if abs(k01 - k23) <= 10 and abs(k12 - k03) <= 10:
            return True
        elif (k01 == float("inf") and k23 == float("inf")) and abs(k12 - k03) <= 10:
            return True
        elif (k12 == float("inf") and k03 == float("inf")) and abs(k01 - k23) <= 10:
            return True
        else:
            return False

    def angle(self, k):
        """由斜率求角度"""
        temp = math.atan(k)
        angle = math.degrees(temp)
        angle = round(angle)
        if angle < 0:
            angle = 180 + angle

        return angle

    def includedAngleCalculate(self, pleft, pmid, pright):
        """计算两直线夹角"""
        kmr = self.getSlope(pmid, pright, 0)
        kml = self.getSlope(pmid, pleft, 0)
        # 求01与02;12与01的夹角
        # （1）存在一条边的斜率不存在时，夹角 = |90-a|
        if kmr == float("inf") or kml == float("inf"):
            if kmr != float("inf"):
                angkmr = self.angle(kmr)
                angmid = abs(90 - angkmr)
            elif kml != float("inf"):
                angkml = self.angle(kml)
                angmid = abs(90 - angkml)
            # print("有垂直，角度为：", angmid)
        else:
            angmid = abs((kml - kmr)/(1+kmr*kml))  # 45度时，ang102=1
            angmid = self.angle(angmid)
            # print("无垂直，角度为：", angmid)
        return angmid

    def triangleJudge(self, vertex):
        """等腰直角三角形判别：求两组夹角是否为45度"""
        ang102 = self.includedAngleCalculate(vertex[2], vertex[0], vertex[1])
        ang210 = self.includedAngleCalculate(vertex[2], vertex[1], vertex[0])
        if abs(ang102 - 45) <= 30 and abs(ang210 - 45) <= 30:
            return True
        else:
            return False
