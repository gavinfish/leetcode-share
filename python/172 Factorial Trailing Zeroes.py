'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n //= 5
            count += n
        return count


if __name__ == "__main__":
    assert Solution().trailingZeroes(25) == 6