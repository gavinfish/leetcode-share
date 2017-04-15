'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

from functools import cmp_to_key


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        sorted_nums = sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        result = ''.join(sorted_nums).lstrip('0')
        return result or '0'


if __name__ == "__main__":
    assert Solution().largestNumber([3, 30, 34, 5, 9]) == '9534330'
    assert Solution().largestNumber([0, 0]) == '0'