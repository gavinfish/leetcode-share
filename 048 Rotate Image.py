'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n):
            for column in range(n - row):
                matrix[row][column], matrix[n - 1 - column][n - 1 - row] = matrix[n - 1 - column][n - 1 - row], \
                                                                           matrix[row][column]
        for row in range(n // 2):
            for column in range(n):
                matrix[row][column], matrix[n - 1 - row][column] = matrix[n - 1 - row][column], matrix[row][column]
        # No need, just to test
        return matrix


if __name__ == "__main__":
    assert Solution().rotate([[1, 2, 3], [8, 9, 4], [7, 6, 5]]) == [[7, 8, 1], [6, 9, 2], [5, 4, 3]]