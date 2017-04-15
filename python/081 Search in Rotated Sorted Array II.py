'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                if nums[left] <= target or nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] > target or nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == "__main__":
    assert Solution().search([4, 5, 5, 6, 7, 0, 1, 2], 4) == True
    assert Solution().search([4, 5, 6, 7, 7, 7, 7, 7, 0, 1, 2], 7) == True