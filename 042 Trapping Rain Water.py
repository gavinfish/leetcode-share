'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        length = len(height)
        maxh = [0 for __ in range(length)]
        h = height[length - 1]
        for i in range(length - 2, -1, -1):
            maxh[i] = h
            h = max(h, height[i])

        h = height[0]
        result = 0
        for i in range(1, length - 1):
            h = max(h, height[i])
            result += max(0, min(h, maxh[i]) - height[i])
        return result


if __name__ == "__main__":
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6