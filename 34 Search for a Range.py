'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        length = len(nums)

        start = 0
        end = length
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if start < length and nums[start] == target:
            result.append(start)
        else:
            return [-1, -1]
        
        end = length
        while start < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid
        result.append(start - 1)

        return result


if __name__ == "__main__":
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]