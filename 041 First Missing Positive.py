'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 0
        length = len(nums)
        while i < length:
            current = nums[i]
            if current <= 0 or current > length or nums[current - 1] == current:
                i += 1
            else:
                nums[current - 1], nums[i] = nums[i], nums[current - 1]

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1


if __name__ == "__main__":
    assert Solution().firstMissingPositive([1, 2, 0]) == 3
    assert Solution().firstMissingPositive([1, 2, 3]) == 4
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2