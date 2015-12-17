'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution(object):
    # Time Limit Exceeded!!!
    def isMatch_timeout(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # When the pattern is None
        if not p:
            return not s
        # When the string is None, pattern like "a*" can still match it
        if not s and p:
            if 1 < len(p) and p[1] == "*":
                return self.isMatch(s, p[2:])
            else:
                return False
        # When the the second character of pattern is "*"
        if 1 < len(p) and p[1] == "*":
            # When the first character matches, there are three possible situation
            if s[0] == p[0] or p[0] == ".":
                return self.isMatch(s[1:], p) or \
                       self.isMatch(s[1:], p[2:]) or \
                       self.isMatch(s, p[2:])
            # Ignore the first two characters in pattern
            else:
                return self.isMatch(s, p[2:])
        else:
            if s[0] == p[0] or p[0] == ".":
                return self.isMatch(s[1:], p[1:])
            else:
                return False


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        # Init dp
        dp = [[False for i in range(n + 1)] for i in range(m + 1)]
        # When string and pattern are all None
        dp[m][n] = True
        # When the string is None, pattern like "a*" can still match it
        for i in range(n - 1, -1, -1):
            if p[i] == "*":
                dp[m][i] = dp[m][i + 1]
            elif i + 1 < n and p[i + 1] == "*":
                dp[m][i] = dp[m][i + 1]
            else:
                dp[m][i] = False

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # When the current character is "*"
                if p[j] == "*":
                    if j - 1 >= 0 and p[j - 1] != "*":
                        dp[i][j] = dp[i][j + 1]
                    # If the pattern is starting with "*" or has "**" in it
                    else:
                        return False
                # When the the second character of pattern is "*"
                elif j + 1 < n and p[j + 1] == "*":
                    # When the current character matches, there are three possible situation
                    # 1. ".*" matches nothing
                    # 2. "c*" matches more than one character
                    # 3. "c*" just matches one character
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i][j + 2] or dp[i + 1][j] or dp[i + 1][j + 2]
                    # Ignore the first two characters("c*") in pattern since they cannot match
                    # the current character in string
                    else:
                        dp[i][j] = dp[i][j + 2]
                else:
                    # When the current character is matched
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = False
        return dp[0][0]


if __name__ == "__main__":
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True