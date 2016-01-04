'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        point = "."
        for i in range(9):
            row = []
            column = []
            diagonal = []
            for j in range(9):
                element = board[i][j]
                if element != point:
                    if element in row:
                        return False
                    else:
                        row.append(element)

                element = board[j][i]
                if element != point:
                    if element in column:
                        return False
                    else:
                        column.append(element)

                element = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if element != point:
                    if element in diagonal:
                        return False
                    else:
                        diagonal.append(element)
        return True