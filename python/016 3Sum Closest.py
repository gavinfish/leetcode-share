'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i = 0
        result = 0
        # Init the distance between result and target with a very large number
        distance = pow(2, 32) - 1
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) == target:
                    return target
                if abs(sum(l) - target) < distance:
                    result = sum(l)
                    distance = abs(sum(l) - target)
                elif sum(l) > target:
                    k -= 1
                else:
                    j += 1
        return result


if __name__ == "__main__":
    assert Solution().threeSumClosest([1, 1, 1, 1], -100) == 3