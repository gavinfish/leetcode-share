'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        dp = [0 for __ in range(length + 1)]
        dp[length] = 1
        dp[length - 1] = 1 if s[length - 1] != '0' else 0
        for i in range(length - 2, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i + 1] + dp[i + 2] if int(s[i:i + 2]) <= 26 else dp[i + 1]
        return dp[0]


if __name__ == "__main__":
    assert Solution().numDecodings("110") == 1
    assert Solution().numDecodings("40") == 0