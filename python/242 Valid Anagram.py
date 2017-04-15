'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = {}
        if len(s) != len(t):
            return False
        for c in s:
            m[c] = m.get(c, 0) + 1
        for c in t:
            if c not in m or m[c] == 0:
                return False
            else:
                m[c] -= 1
        return True


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    assert Solution().isAnagram(s, t) == True
    s, t = 'rat', 'car'
    assert Solution().isAnagram(s, t) == False
