'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for num in nums:
            # calculate the count of the each bit
            three = two & num
            two = two | one & num
            one = one | num
            # clear the count for the bit which has achieved three
            one = one & ~three
            two = two & ~three
        return one

    def singleNumber_normal(self, nums):
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            rem = count % 3
            # deal with the negative situation
            if i == 31 and rem:
                result -= 1 << 31
            else:
                result |= rem << i
        return result


if __name__ == "__main__":
    assert Solution().singleNumber([1, 1, 1, 2, 3, 3, 3]) == 2
    assert Solution().singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]) == -4
    assert Solution().singleNumber_normal([1, 1, 1, 2, 3, 3, 3]) == 2
    assert Solution().singleNumber_normal([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]) == -4