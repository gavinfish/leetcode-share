'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for __ in range(n + 1)]
        for i in range(2, n + 1):
            s = 0
            for j in range(i):
                s += dp[j] * dp[i - 1 - j]
            dp[i] = s
        return dp[-1]


if __name__ == "__main__":
    assert Solution().numTrees(5) == 42