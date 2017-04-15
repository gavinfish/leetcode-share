'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
'''

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = ((n & 0x55555555) << 1) | ((n >> 1) & 0x55555555)
        n = ((n & 0x33333333) << 2) | ((n >> 2) & 0x33333333)
        n = ((n & 0x0f0f0f0f) << 4) | ((n >> 4) & 0x0f0f0f0f)
        n = (n << 24) | ((n & 0xff00) << 8) | ((n >> 8) & 0xff00) | (n >> 24)
        return n & 0xffffffff


if __name__ == "__main__":
    assert Solution().reverseBits(43261596) == 964176192