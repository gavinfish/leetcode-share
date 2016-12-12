'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, m, count = n, 1, 0
        while x > 0:
            lastDigit = x % 10
            x //= 10
            count += x * m
            if lastDigit == 1:
                count += n % m + 1
            elif lastDigit > 1:
                count += m
            m *= 10
        return count


if __name__ == "__main__":
    assert Solution().countDigitOne(13) == 6
