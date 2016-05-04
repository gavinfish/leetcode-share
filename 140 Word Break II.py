'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''

import collections


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dic = collections.defaultdict(list)

        def dfs(s):
            if not s:
                return [None]
            if s in dic:
                return dic[s]
            res = []
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    for r in dfs(s[n:]):
                        if r:
                            res.append(word + " " + r)
                        else:
                            res.append(word)
            dic[s] = res
            return res

        return dfs(s)


if __name__ == "__main__":
    assert Solution().wordBreak("catsanddog", {"cat", "cats", "and", "sand", "dog"}) == ['cat sand dog', 'cats and dog']