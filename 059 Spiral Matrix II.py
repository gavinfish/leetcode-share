'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left = top = 0
        right = n - 1
        bottom = n - 1
        num = 1
        result = [[0 for __ in range(n)] for __ in range(n)]
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            for i in range(top, bottom):
                result[i][right] = num
                num += 1
            for i in range(right, left, -1):
                result[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                result[i][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            result[top][left] = num
        return result


if __name__ == "__main__":
    assert Solution().generateMatrix(5) == [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7],
                                            [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]