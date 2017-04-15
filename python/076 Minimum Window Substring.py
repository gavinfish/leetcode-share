'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        MAX_INT = 2147483647
        start = end = 0
        char_need = defaultdict(int)    # the count of char needed by current window, negative means current window has it but not needs it
        count_need = len(t)             # count of chars not in current window but in t
        min_length = MAX_INT
        min_start = 0
        for i in t:
            char_need[i] += 1           # current window needs all char in t
        while end < len(s):
            if char_need[s[end]] > 0:
                count_need -= 1
            char_need[s[end]] -= 1      # current window contains s[end] now, so does not need it any more
            end += 1
            while count_need == 0:
                if min_length > end - start:
                    min_length = end - start
                    min_start = start
                char_need[s[start]] += 1    # current window does not contain s[start] any more
                if char_need[s[start]] > 0: # when some count in char_need is positive, it means there is char in t but not current window
                    count_need += 1
                start += 1
        return "" if min_length == MAX_INT else s[min_start:min_start + min_length]


if __name__ == "__main__":
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"