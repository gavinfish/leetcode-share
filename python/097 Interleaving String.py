'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        dp = [True for __ in range(m + 1)]
        for i in range(m):
            dp[i + 1] = dp[i] and s1[i] == s3[i]
        for j in range(n):
            dp[0] = dp[0] and s2[j] == s3[j]
            for i in range(m):
                dp[i + 1] = (dp[i] and s1[i] == s3[i + j + 1]) or (dp[i + 1] and s2[j] == s3[i + j + 1])
        return dp[m]


if __name__ == "__main__":
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False