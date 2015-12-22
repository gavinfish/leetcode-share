'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, "", result)
        return result

    def generate(self, left, right, str, result):
        if left == 0 and right == 0:
            result.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + "(", result)
        if right > left:
            self.generate(left, right - 1, str + ")", result)


if __name__ == "__main__":
    assert (Solution().generateParenthesis(3)) == ['((()))', '(()())', '(())()', '()(())', '()()()']
