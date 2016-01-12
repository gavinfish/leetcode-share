'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # To print the result
    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if not intervals:
            return result
        intervals.sort(key=lambda x: x.start)
        result.append(intervals[0])
        for interval in intervals[1:]:
            prev = result[-1]
            if prev.end >= interval.start:
                prev.end = max(prev.end, interval.end)
            else:
                result.append(interval)
        return result


if __name__ == "__main__":
    intervals = Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
    for interval in intervals:
        print(interval)