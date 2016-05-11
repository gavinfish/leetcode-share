'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        mid = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[mid]


if __name__ == "__main__":
    assert Solution().findMin([1, 2, 3, 4, 5]) == 1
    assert Solution().findMin([2, 3, 4, 5, 1]) == 1
    assert Solution().findMin([5, 1, 2, 3, 4]) == 1