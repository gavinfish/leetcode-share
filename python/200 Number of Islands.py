'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i + 1, j)
                return 1
            return 0

        count = sum(dfs(i, j) for i in range(n) for j in range(m))
        return count


if __name__ == "__main__":
    assert Solution().numIslands([['1', '1', '0', '0', '0'],
                                  ['1', '1', '0', '0', '0'],
                                  ['0', '0', '1', '0', '0'],
                                  ['0', '0', '0', '1', '1']]) == 3