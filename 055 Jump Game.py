'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        index = 0
        longest = nums[0]
        while index <= longest:
            if longest >= length - 1:
                return True
            longest = max(longest, index + nums[index])
            index += 1
        return False


if __name__ == "__main__":
    assert Solution().canJump([2, 3, 1, 1, 4]) == True
    assert Solution().canJump([3, 2, 1, 0, 4]) == False