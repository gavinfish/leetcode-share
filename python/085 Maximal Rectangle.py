'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0 for __ in range(n + 1)]
        result = 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    result = max(result, h * w)
                stack.append(i)
        return result


if __name__ == "__main__":
    assert Solution().maximalRectangle([['1', '1', '0', '1', '0', '1'],
                                        ['0', '1', '0', '0', '1', '1'],
                                        ['1', '1', '1', '1', '0', '1'],
                                        ['1', '1', '1', '1', '0', '1']]) == 8