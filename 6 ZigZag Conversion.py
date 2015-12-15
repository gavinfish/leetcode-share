'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        result = ''
        index = 0
        n = len(s)
        for i in range(0, numRows):
            if i == 0 or i == numRows - 1:
                while index < n:
                    result += s[index]
                    index += 2 * numRows - 2
                index = i + 1
            else:
                while index < n:
                    result += s[index]
                    index += 2 * numRows - 2 * i - 2
                    if index >= n:
                        break
                    result += s[index]
                    index += 2 * i
                index = i + 1
        return result

# Test cases
if __name__ == "__main__":
    Solution().convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
    Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"