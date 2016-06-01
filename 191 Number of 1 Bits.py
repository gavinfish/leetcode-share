'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= (n >> 1) & 0x55555555
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n + (n >> 4)) & 0x0f0f0f0f
        n += (n >> 8)
        n += (n >> 16)
        return n & 0x3f


if __name__ == "__main__":
    assert Solution().hammingWeight(4294967295) == 32
    assert Solution().hammingWeight(11) == 3