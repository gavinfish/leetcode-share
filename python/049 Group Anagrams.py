'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for i, v in enumerate(strs):
            target = "".join(sorted(v))
            if target not in map:
                map[target]=[v]
            else:
                map[target].append(v)

        result = []
        for value in map.values():
            result += [sorted(value)]
        return result


if __name__ == "__main__":
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['nat', 'tan'], ['bat'],
                                                                                    ['ate', 'eat', 'tea']]