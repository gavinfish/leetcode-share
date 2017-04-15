'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        base = ord('A')
        while n:
            n, r = divmod(n - 1, 26)
            result.append(chr(base + r))
        return ''.join(result[::-1])


if __name__ == "__main__":
    assert Solution().convertToTitle(1) == 'A'
    assert Solution().convertToTitle(28) == 'AB'