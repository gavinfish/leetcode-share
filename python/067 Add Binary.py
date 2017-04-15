'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = val = 0
        if len(a) < len(b):
            a, b = b, a
        lengthA = len(a)
        lengthB = len(b)
        for i in range(lengthA):
            val = carry
            val += int(a[-(i + 1)])
            if i < lengthB:
                val += int(b[-(i + 1)])
            carry, val = val // 2, val % 2
            result.append(str(val))
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])


if __name__ == "__main__":
    assert Solution().addBinary("111", "1") == "1000"