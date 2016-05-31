'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord('A') - 1
        n = len(s)
        result = 0
        for i in range(n):
            result += (ord(s[n - 1 - i]) - base) * pow(26, i)
        return result


if __name__ == "__main__":
    assert Solution().titleToNumber('A') == 1
    assert Solution().titleToNumber('AB') == 28