'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        length1 = len(num1)
        length2 = len(num2)
        temp = [0 for __ in range(length1 + length2)]
        # Do multiply
        for i in range(length1):
            for j in range(length2):
                temp[i + j] += int(num1[i]) * int(num2[j])
        carry = 0
        digits = []
        # Do plus
        for num in temp:
            s = carry + num
            carry = s // 10
            digits.append(str(s % 10))
        result = "".join(digits)[::-1]
        # Remove the surplus zero
        sub_index = 0
        for i in range(length1 + length2 - 1):
            if result[i] == "0":
                sub_index += 1
            else:
                break
        result = result[sub_index:]
        return result


if __name__ == "__main__":
    assert Solution().multiply("120", "20000") == 2400000
    assert Solution().multiply("0", "3421") == 0