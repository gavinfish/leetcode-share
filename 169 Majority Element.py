'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        count = 0
        for num in nums:
            if count == 0:
                result = num
            if result == num:
                count += 1
            else:
                count -= 1
        return result


if __name__ == "__main__":
    assert Solution().majorityElement([1, 2, 2, 3, 3, 3, 3]) == 3
    assert Solution().majorityElement([3, 3, 3, 3, 1, 1, 2]) == 3