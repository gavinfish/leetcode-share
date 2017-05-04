'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''


class Solution(object):
    def longestPalindrome2(self, s):
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
        # Whether the substring contains the first character or last character
        # and is palindromic
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

    def longestPalindrome(self, s):
        string = "#" + "#".join(s) + "#"
        i = 0
        maxBorder = 0  # store the max border that has been reached
        maxCenter = 0  # the center of palindrome that has been largest for now
        p = [0 for _ in range(len(string))]  # min in (center to i or i to border)
        res = [0, 0]

        while i < len(string):
            p[i] = min(p[2 * maxCenter - i], maxBorder - i) if maxBorder > i else 1
            while i - p[i] >= 0 and i + p[i] < len(string) and string[i - p[i]] == string[i + p[i]]:
                p[i] += 1
            if maxBorder < p[i] + i:
                maxBorder = p[i] + i
                maxCenter = i
                if maxBorder - maxCenter > res[1] - res[0]:
                    res = [maxCenter, maxBorder]
            i += 1

        return "".join([x for x in string[2 * res[0] - res[1] + 1:res[1]] if x != '#'])


if __name__ == "__main__":
    assert Solution().longestPalindrome("aba") == "aba"
    assert Solution().longestPalindrome("abba") == "abba"
    assert Solution().longestPalindrome("xaba") == "aba"
    assert Solution().longestPalindrome("xabba") == "abba"
