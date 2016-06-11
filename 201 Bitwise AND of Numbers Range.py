'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while n > m:
            n &= n - 1
        return n


if __name__ == "__main__":
    assert Solution().rangeBitwiseAnd(5, 7) == 4
    assert Solution().rangeBitwiseAnd(7, 15) == 0