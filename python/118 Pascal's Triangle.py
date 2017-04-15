'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        result = [[1]]
        while numRows > 1:
            result.append([1] + [a + b for a, b in zip(result[-1][:-1], result[-1][1:])] + [1])
            numRows -= 1
        return result


if __name__ == "__main__":
    assert Solution().generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]