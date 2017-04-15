'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                if i - m.get(nums[i]) <= k:
                    return True
            m[nums[i]] = i
        return False


if __name__ == "__main__":
    assert Solution().containsNearbyDuplicate([1, 2, 3, 4], 1) == False
    assert Solution().containsNearbyDuplicate([1, 1, 2, 3], 2) == True
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 2) == False