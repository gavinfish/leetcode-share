'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_index, s_index, last_s_index, last_p_index = 0, 0, -1, -1
        while s_index < len(s):
            # Normal match including '?'
            if p_index < len(p) and (s[s_index] == p[p_index] or p[p_index] == '?'):
                s_index += 1
                p_index += 1
            # Match with '*'
            elif p_index < len(p) and p[p_index] == '*':
                p_index += 1
                last_s_index = s_index
                last_p_index = p_index
            # Not match, but there is a '*' before
            elif last_p_index != -1:
                last_s_index += 1
                s_index = last_s_index
                p_index = last_p_index
            # Not match and there is no '*' before
            else:
                return False
        # Check if there is still character except '*' in the pattern
        while p_index < len(p) and p[p_index] == '*':
            p_index += 1
        # If finish scanning both string and pattern, then it matches well
        return p_index == len(p)


if __name__ == "__main__":
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", "*") == True
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("ab", "?*") == True
    assert Solution().isMatch("aab", "c*a*b") == False