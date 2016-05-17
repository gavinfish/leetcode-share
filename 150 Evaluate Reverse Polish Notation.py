'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                else:
                    if first * second < 0:
                        stack.append(-(abs(first) // abs(second)))
                    else:
                        stack.append(first // second)
        return stack.pop()


if __name__ == "__main__":
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22