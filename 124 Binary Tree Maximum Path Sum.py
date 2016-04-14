'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        self._maxPathSum(root)
        return self.maxSum

    def _maxPathSum(self, root):
        if root is None:
            return 0
        left = self._maxPathSum(root.left)
        right = self._maxPathSum(root.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.maxSum = max(self.maxSum, root.val + left + right)
        return max(left, right) + root.val