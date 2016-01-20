'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = path.split("/")
        result = ['']
        for part in parts:
            if part:
                if part not in ('.', '..'):
                    if len(result) == 0:
                        result.append('')
                    result.append(part)
                elif part == '..' and len(result) > 0:
                    result.pop()
        if len(result) < 2:
            return "/"
        else:
            return "/".join(result)


if __name__ == "__main__":
    assert Solution().simplifyPath("/a/./b/../../c/") == '/c'
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/../../") == "/"