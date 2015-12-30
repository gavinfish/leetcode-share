'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = len(s)
        dp = [0 for __ in range(length)]
        for i in range(1, length):
            if s[i] == ")":
                j = i - 1 - dp[i - 1]
                if j >= 0 and s[j] == "(":
                    dp[i] = dp[i - 1] + 2
                    if j - 1 >= 0:
                        dp[i] += dp[j - 1]
        return max(dp)


if __name__ == "__main__":
    assert Solution().longestValidParentheses("(()))())(") == 4
    assert Solution().longestValidParentheses("(()") == 2
    assert Solution().longestValidParentheses(")()())") == 4
