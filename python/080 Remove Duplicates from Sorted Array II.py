'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if count < 2 or nums[count - 2] != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == "__main__":
    l = [1, 1, 1, 2, 2, 3]
    r = Solution().removeDuplicates(l)
    assert l == [1, 1, 2, 2, 3, 3]
    assert r == 5