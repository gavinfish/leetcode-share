'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset, maxlen = set(nums), 0
        for n in set(nums):
            currlen, tmp = 1, n + 1
            while tmp in numset:
                currlen += 1
                numset.discard(tmp)
                tmp += 1
            tmp = n - 1
            while tmp in numset:
                currlen += 1
                numset.discard(tmp)
                tmp -= 1
            maxlen = max(maxlen, currlen)
        return maxlen


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4