'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp = [0 for __ in range(n + 1)]
        dp[0] = 1
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if t[j] == s[i]:
                    dp[j + 1] += dp[j]
        return dp[-1]


if __name__ == "__main__":
    assert Solution().numDistinct("rabbbit", "rabbit") == 3