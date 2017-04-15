'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]
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
    def insert(self, intervals, newInterval):
        start, end = newInterval.start, newInterval.end
        left = list(filter(lambda x: x.end < start, intervals))
        right = list(filter(lambda x: x.start > end, intervals))
        if len(left) + len(right) != len(intervals):
            start = min(start, intervals[len(left)].start)
            end = max(end, intervals[-len(right) - 1].end)

        return left + [Interval(start, end)] + right


if __name__ == "__main__":
    intervals = Solution().insert([Interval(2, 6), Interval(8, 10), Interval(15, 18)], Interval(13, 16))
    for interval in intervals:
        print(interval)