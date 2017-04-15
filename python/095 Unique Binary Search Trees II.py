'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        self.cache = {}
        return self._generateTrees(1, n)

    def _generateTrees(self, start, end):
        if (start, end) not in self.cache:
            roots = []
            for root in range(start, end + 1):
                for left in self._generateTrees(start, root - 1):
                    for right in self._generateTrees(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        roots.append(node)
            self.cache[(start, end)] = roots
        return self.cache[(start, end)] or [None]


if __name__ == "__main__":
    None