'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        result = []
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                for r in self.partition(s[i + 1:]):
                    result.append([s[:i + 1]] + r)
        return result

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    assert Solution().partition("aab") == [
        ["a", "a", "b"],
        ["aa", "b"]
    ]