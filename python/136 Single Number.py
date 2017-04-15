'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in nums[1:]:
            result ^= i
        return result


if __name__ == "__main__":
    assert Solution().singleNumber([1, 2, 3, 4, 3, 2, 1]) == 4