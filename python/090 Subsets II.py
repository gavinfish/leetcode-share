'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Subscribe to see which companies asked this question
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        temp_size = 0
        for i in range(len(nums)):
            start = temp_size if i >= 1 and nums[i] == nums[i - 1] else 0
            temp_size = len(result)
            for j in range(start, temp_size):
                result.append(result[j] + [nums[i]])
        return result


if __name__ == "__main__":
    assert Solution().subsetsWithDup([1, 2, 2]) == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]