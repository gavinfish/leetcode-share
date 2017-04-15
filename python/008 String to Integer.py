'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # Check None situation
        if not str:
            return 0
        # Check only whitespace situation
        str = str.strip()
        if not str:
            return 0
        flag = 1
        if str[0] in ['+', '-']:
            if str[0] == '-':
                flag = -1
            str = str[1:]
        # Check "+","-" situation and the first char is not number
        if not str or not str[0].isdigit():
            return 0
        # Ignore all char after the first no-number char
        for i, v in enumerate(str):
            if not v.isdigit():
                str = str[:i]
                break
        result = 0
        for v in str[:]:
            result += ord(v) - ord('0')
            result *= 10
        result /= 10
        result *= flag
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result


if __name__ == "__main__":
    assert Solution().myAtoi(" -1123") == -1123
    assert Solution().myAtoi("222222222222222") == 2147483647