'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        sign = 1
        if dividend >= 0 and divisor < 0 or dividend <= 0 and divisor > 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        current = divisor
        currentResult = 1
        while current <= dividend:
            current <<= 1
            currentResult <<= 1
        while divisor <= dividend:
            current >>= 1
            currentResult >>= 1
            if current <= dividend:
                dividend -= current
                result += currentResult
        return min(sign * result, MAX_INT)


if __name__ == "__main__":
    assert Solution().divide(5, -1) == -5
    assert Solution().divide(10, 2) == 5