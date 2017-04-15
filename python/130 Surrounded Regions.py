'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        n = len(board)
        m = len(board[0])
        queue = []
        # Get all 'O' on edge
        for i in range(n):
            for j in range(m):
                if ((i in (0, n - 1)) or (j in (0, m - 1))) and board[i][j] == 'O':
                    queue.append((i, j))
        # Mark all 'O' which can connect to 'O' on edge
        while queue:
            r, c = queue.pop(0)
            if 0 <= r < n and 0 <= c < m and board[r][c] == 'O':
                board[r][c] = 'M'
                if r - 1 >= 0 and board[r - 1][c] == 'O':
                    queue.append((r - 1, c))
                if r + 1 < n and board[r + 1][c] == 'O':
                    queue.append((r + 1, c))
                if c - 1 >= 0 and board[r][c - 1] == 'O':
                    queue.append((r, c - 1))
                if c + 1 < m and board[r][c + 1] == 'O':
                    queue.append((r, c + 1))
        # Update characters
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    expected_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    assert board == expected_board