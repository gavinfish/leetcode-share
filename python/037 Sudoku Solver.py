'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
'''


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for row in range(9):
            board[row] = list(board[row])
        self.recursive(0, 0, board)
        for row in range(9):
            board[row] = "".join(board[row])

    def recursive(self, i, j, board):
        if j >= 9:
            return self.recursive(i + 1, 0, board)
        if i == 9:
            return True

        if board[i][j] == ".":
            for num in range(1, 10):
                num_str = str(num)
                if all([board[i][col] != num_str for col in
                        range(9)]) and all([board[row][j] != num_str for row in range(9)]) and all(
                    [board[i // 3 * 3 + count // 3][j // 3 * 3 + count % 3] != num_str for count in
                     range(9)]):
                    board[i][j] = num_str
                    if not self.recursive(i, j + 1, board):
                        board[i][j] = "."
                    else:
                        return True
        else:
            return self.recursive(i, j + 1, board)
        return False


if __name__ == "__main__":
    sudoku = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
              "...2759.."]
    Solution().solveSudoku(sudoku)
    assert sudoku == ['519748632', '783652419', '426139875', '357986241', '264317598', '198524367', '975863124',
                      '832491756', '641275983']
