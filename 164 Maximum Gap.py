'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def radix_sort(nums):
            max_num = max(nums)
            i = 1
            while max_num // i:
                buckets = [[] for __ in range(10)]
                for num in nums:
                    buckets[((num // i) % 10)].append(num)
                nums = [num for bucket in buckets for num in bucket]
                i *= 10
            return nums

        n = len(nums)
        if n < 2:
            return 0
        nums = radix_sort(nums)
        max_gap = 0
        for i in range(1, n):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        return max_gap


if __name__ == "__main__":
    assert Solution().maximumGap([99, 50, 3, 18, 28]) == 49