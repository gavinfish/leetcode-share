'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        slope_map = {}
        result = 0
        for i in range(n):
            slope_map.clear()
            same, vertical = 1, 0
            slope_max = 0
            for j in range(i + 1, n):
                dx, dy = points[i].x - points[j].x, points[i].y - points[j].y
                if dx == dy == 0:
                    same += 1
                elif dx == 0:
                    vertical += 1
                else:
                    slope = float(dy) / float(dx)
                    slope_map[slope] = slope_map.get(slope, 0) + 1
                    slope_max = max(slope_max, slope_map[slope])
            result = max(result, max(slope_max, vertical) + same)
        return result


if __name__ == "__main__":
    None