'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        result = set()
        sumsIndexes = {}
        # Get all two elements' sum and indexes map
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] in sumsIndexes:
                    sumsIndexes[nums[i] + nums[j]].append((i, j))
                else:
                    sumsIndexes[nums[i] + nums[j]] = [(i, j)]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sumNeeded = target - (nums[i] + nums[j])
                if sumNeeded in sumsIndexes:
                    for index in sumsIndexes[sumNeeded]:
                        if index[0] > j:
                            result.add(tuple(sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]])))
        # Format result with list[list] pattern
        result = [list(l) for l in result]
        return result


if __name__ == "__main__":
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-1, 0, 0, 1], [-2, 0, 0, 2], [-2, -1, 1, 2]]
