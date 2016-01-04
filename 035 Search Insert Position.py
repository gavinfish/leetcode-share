'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        start = 0
        end = length
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target or (nums[mid] > target and (mid == 0 or nums[mid - 1] < target)):
                return mid
            if mid == length - 1 and nums[mid] < target:
                return mid + 1
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid


if __name__ == "__main__":
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0