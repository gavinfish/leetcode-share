'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return
        n = len(s)
        if n == 1:
            return s
        # Left index of the target substring
        l = 0
        # Right index of the target substring
        r = 0
        # Length of the longest palindromic substring for now
        m = 0
        # Length of the current substring
        c = 0
        #  Whether the substring contains the first character or last character and is palindromic
        b = True
        for i in range(0, n):
            # Odd situation
            for j in range(0, min(n - i, i + 1)):
                if (s[i - j] != s[i + j]):
                    b = False
                    break
                else:
                    c = 2 * j + 1
            if (c > m):
                l = i - j + 1 - b
                r = i + j + b
                m = c
            b = True
            # Even situation
            for j in range(0, min(n - i - 1, i + 1)):
                if (s[i - j] != s[i + j + 1]):
                    b = False
                    break
                else:
                    c = 2 * j + 2
            if (c > m):
                l = i - j + 1 - b
                r = i + j + 1 + b
                m = c
            b = True
        return s[l:r]



if __name__ == "__main__":
    assert Solution().longestPalindrome("aba") == "aba"
    assert Solution().longestPalindrome("abba") == "abba"
    assert Solution().longestPalindrome("xaba") == "aba"
    assert Solution().longestPalindrome("xabba") == "abba"
