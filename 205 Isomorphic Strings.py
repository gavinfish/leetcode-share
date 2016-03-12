'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        found = {}
        for c1, c2 in zip(s, t):
            if c1 in found:
                if not found[c1] == c2:
                    return False
            else:
                if c2 in found.values():
                    return False
                found[c1] = c2
        return True


if __name__ == "__main__":
    assert Solution().isIsomorphic("egg", "add") == True
    assert Solution().isIsomorphic("foo", "bar") == False
    assert Solution().isIsomorphic("paper", "title") == True