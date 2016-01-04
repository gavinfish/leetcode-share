'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        for i in range(len(s)):
            if i > 0 and map[s[i]] > map[s[i - 1]]:
                result -= map[s[i - 1]]
                result += map[s[i]] - map[s[i - 1]]
            else:
                result += map[s[i]]
        return result

# Test cases
if __name__ == "__main__":
    assert Solution().romanToInt("XII") == 12
    assert Solution().romanToInt("XXI") == 21
    assert Solution().romanToInt("XCIX") == 99