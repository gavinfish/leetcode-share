'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ''
        for i in range(len(nums)):
            while num >= nums[i]:
                num -= nums[i]
                result += strings[i]
        return result

# Test cases
if __name__ == "__main__":
    assert Solution().intToRoman(12) == "XII"
    assert Solution().intToRoman(21) == "XXI"
    assert Solution().intToRoman(99) == "XCIX"