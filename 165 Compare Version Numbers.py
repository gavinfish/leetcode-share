'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_list = version1.split(".")
        version2_list = version2.split(".")
        len1 = len(version1_list)
        len2 = len(version2_list)
        for i in range(max(len1, len2)):
            v1 = int(version1_list[i]) if i < len1 else 0
            v2 = int(version2_list[i]) if i < len2 else 0
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0


if __name__ == "__main__":
    assert Solution().compareVersion("0.1", "1.1") == -1
    assert Solution().compareVersion("01.2", "1.1") == 1
    assert Solution().compareVersion("2.3", "2.3") == 0